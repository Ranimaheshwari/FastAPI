FROM python

WORKDIR /postgres_blog

ENV PYTHONPATH "${PYTHONPATH}:/postgres_blog"

EXPOSE 8000

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn" , "postgres_blog.main:app" , "--port" , "8000", "--reload"]

