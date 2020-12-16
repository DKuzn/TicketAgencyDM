docker build --tag ticketagency -f Dockerfile .

docker run --name ticketagency -p 5432:5432 -e POSTGRES_PASSWORD=mypass -d ticketagency