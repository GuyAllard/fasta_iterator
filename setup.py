from setuptools import setup

setup(name="fasta_iterator",
      version="1.0.0",
      description="Simple iterator to generate sequence records from a fasta file",
      author="Guy Allard",
      author_email="guyallard01 AT gmail DOT com",
      url="https://github.com/GuyAllard/fasta_iterator",
      license="MIT",
      platforms=['any'],
      packages=["fasta_iterator"],
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'License :: MIT License',
      ],
      keywords = 'bioinformatics'
)
