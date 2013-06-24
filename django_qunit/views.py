import os
from django.shortcuts import render_to_response
from django.conf import settings
from django.utils import simplejson
from django.contrib.staticfiles.finders import AppDirectoriesFinder, FileSystemFinder


def get_suite_context(request, path):
    """Use path to find all static files and templates
    that belong here """

    directories, files = walk_finders(path)

    suite = {}

    # Set suite name
    pieces = path.split('/')
    if len(pieces) < 2:
        suite['name'] = pieces[0] or 'main'
    else:
        suite['name'] = pieces[-2]
    
    # Format suite name
    suite['name'] = pretty_variable(suite['name'])

    # Format directories too
    subsuites = [{"link_name": d, "pretty_name": pretty_variable(d)} for d in directories]

    # Set suite defaults
    suite['extra_urls'] = []
    suite['extra_media_urls'] = []

    # Load suite.json if present
    for file in files:
        if 'suite.json' in file[0]:
          fileo = file[1]._open(name = file[0], mode='rb')
          json = fileo.read()
          suite.update(simplejson.loads(json))

    previous_directory = parent_directory(path)
    
    return {
        'files': [file[0] for file in files if file[0].endswith('js')],
        'html_stubs': [{'path': file[1].path(file[0]), 'file': os.path.basename(file[0]).rstrip(".html")}
                        for file in files if file[0].endswith('html')],
        'previous_directory': previous_directory,
        'in_subdirectory': True and (previous_directory is not None) or False,
        'subsuites': subsuites,
        'suite': suite,
    }


def pretty_variable(name):
    """Replace underscores with spaces and capitalize each word """
    return name.replace("_", " ").title()


def walk_finders(path):
  """Find all qunit related files given the path component that comes
  after '/qunit/'

  Works similarly to 'os.walk' but returns just files and directories
  by surfing over all possible files.
  """
  # Get a file system path from url path
  path_comps = [c for c in path.split('/') if c != u'']
  tmp = os.sep.join(path_comps)
  file_path = os.path.join(settings.QUNIT_TEST_PATH, tmp)
  finder_files = []

  # Get list of files from app directories from app file finder
  adf = AppDirectoriesFinder()
  for fpath, filestorageobj in adf.list(''):
    if settings.QUNIT_TEST_PATH in fpath:
      finder_files.append((fpath, filestorageobj))

  # Get list of files from app directories from file system file finder
  # By adding this second, files in the project base override app specific files
  fsf = FileSystemFinder()
  for fpath, filestorageobj in fsf.list(''):
    if settings.QUNIT_TEST_PATH in fpath:
      finder_files.append((fpath, filestorageobj))

  # Form arrays of files in this directory and sub directories
  matchfiles = []
  subdirectories = []
  for ffile_path, fso in finder_files:
      split = ffile_path.split(file_path)
      if len(split) > 1:
          # Check to see if sub-directories exist
          path_split = split[1].split(os.sep)
          if len(path_split) > 1 and path_split[0] != u'':
              # this file indicates a sub directory
              subdirectories.append(path_split[0])
          else:
              # this is a file in this directory
              matchfiles.append((ffile_path, fso))

  # Get rid of duplicates
  subdirectories = list(set(subdirectories)) # array of strings
  matchfiles = list(set(matchfiles)) # array of tuples
  
  return (subdirectories, matchfiles)


def run_tests(request, path):
    suite_context = get_suite_context(request, path)
    return render_to_response('qunit/index.html', suite_context)

    
def parent_directory(path):
    """
    Get parent directory. If root, return None
    "" => None
    "foo/" => "/"
    "foo/bar/" => "foo/"
    """
    if path == '':
        return None
    prefix = '/'.join(path.split('/')[:-2])
    if prefix != '':
        prefix += '/'
    return prefix
