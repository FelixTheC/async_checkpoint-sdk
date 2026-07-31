for filename in ./apis/*
do
  echo "generare docs for " ${filename}
  gendocs_new ${filename}
done