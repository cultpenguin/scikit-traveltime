from distutils.core import setup
setup(
  name = 'scikit-traveltime',
  packages = ['scikit-traveltime'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Traveltime compuation based on the eikonal equation',
  author = 'Thomas Mejer Hansen',
  author_email = 'thomas.mejer.hansen@gmail.com',
  url = 'https://github.com/cultpenguin/scikit-traveltime', # use the URL to the github repo
  download_url = 'https://github.com/cultpenguin/scikit-traveltime/archive/master.zip', # I'll explain this in a second
  keywords = ['traveltime', 'eikonal', 'fast-marching'], # arbitrary keywords
  classifiers = [],
)

#  install_requires = ['numpy >= 1.0.2', 'scikit-fmm>0.9'],
