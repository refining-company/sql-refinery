# General SQL
curl -LO https://github.com/DerekStride/tree-sitter-sql/archive/refs/heads/gh-pages.tar.gz
tar -xzf gh-pages.tar.gz
cd tree-sitter-sql-gh-pages

cc -shared -fPIC -I./src src/parser.c src/scanner.c -o ../sql.so

rm -rf ../tree-sitter-sql-gh-pages
rm -f ../gh-pages.tar.gz