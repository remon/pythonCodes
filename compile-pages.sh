echo 'Cleaning documentation_utils directory'
rm -rf documentation_utils/*

echo 'Copying the README over to the pages'
cat README.md >> documentation_utils/index.md

echo 'Compiling pages from python to markdown content'
python3 python_to_markdown_compiler.py

echo 'Building the documentation'
mkdocs build --clean
