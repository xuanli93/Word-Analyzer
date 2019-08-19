Focal Coding Challenge - Oliver Twist

Part I

  Please find a gzipped version of Charles Dickens' Oliver Twist novel
  from project Gutenberg.  The challenge is to build a HTTP app that will:
    - accept an uncompressed file as an upload (accept any text UTF-8 file)
    - compute a frequency count for each word in the file (a word is defined
      as any string of consecutive non-whitespace chars (refer to
      string.whitespace for definition of whitespace characters).
    - output the frequency distribution in a HTML table sorted most
      frequent to least.
    - please use python (2 or 3 is OK) and Flask for your HTTP app
      (https://flask.palletsprojects.com/en/1.0.x/).

  When returning your code, please include only the python source code
  and any requirements.txt you feel will be needed to run your package.
  Please also include the histogram output as a single .html file.

  Please pay attention to things like style, variable names and docstrings.


Part II

  Now please imagine that there are one million clients sending 20 blobs a
  day to the service from part I.   Each blob averages 1MB in size.  Briefly
  sketch a cloud deployment that can handle this traffic.   How many replicas
  would be needed to keep from falling behind?  How much total RAM,CPU,network
  resources would be required?  What sort of monitoring would be helpful for
  a production service?   Where are the bottlenecks and points of failure?
  What will need to change for 100 million clients?



Thank you for your efforts.
