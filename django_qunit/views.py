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

    # set suite name
    pieces = path.split('/')
    if len(pieces) < 2:
        suite['name'] = pieces[0] or 'main'
    else:
        suite['name'] = pieces[-2]

    # defaults
    suite['extra_urls'] = []
    suite['extra_media_urls'] = []

    # load suite.json if present
    if 'suite.json' in files:
        file = open(os.path.join(full_path, 'suite.json'), 'r')
        json = file.read()
        suite.update(simplejson.loads(json))

    previous_directory = parent_directory(path)
    
    return {
        'files': [path + file for file in files if file.endswith('js')],
        'html_stubs': [{'path': path + file, 'file': file} for file in files if file.endswith('html')],
        'previous_directory': previous_directory,
        'in_subdirectory': True and (previous_directory is not None) or False,
        'subsuites': directories,
        'suite': suite,
    }


def walk_finders(path):
  """Find all qunit related files given the path component that comes
  after '/qunit/'

  Works similarly to 'os.walk' but returns just files and directories
  by surfing over all possible files.
  """
  finder_files = []

  # Get list of files from app directories from app file finder
  adf = AppDirectoriesFinder()
  for fpath, _ in adf.list(''):
    if 'qunit' in fpath:
      finder_files.append(fpath)

  # Get list of files from app directories from file system file finder
  # By adding this second, files in the project base override apop specific files
  fsf = FileSystemFinder()
  for fpath, _ in fsf.list(''):
    if 'qunit' in fpath:
      finder_files.append(fpath)

  # Form arrays of files in this directory and sub directories
  matchfiles = []
  subdirectories = []
  for file_path in finder_files:
      urlpath = os.path.join("qunit", path)
      split = file_path.split(urlpath)
      if len(split) > 1:
          # check to see if sub-directories exist
          path_split = split[1].split(os.sep)
          if len(path_split) > 1:
              # this file indicates a sub directory
              subdirectories.append(path_split[0])
          else:
              # this is a file in this directory
              matchfiles.append(file_path)

  # Get rid of duplicates
  subdirectories = list(set(subdirectories))
  matchfiles = list(set(matchfiles))
  
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
