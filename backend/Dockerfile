From rakaim/pytesseract

WORKDIR /app/src
COPY . /app
CMD cp ./data/chi_sim.traineddata /usr/share/tesseract-ocr/4.00/tessdata

RUN pip3 install -r /app/requirments.txt -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

# CMD gunicorn --bind 0.0.0.0:5000 -w 2 app:app --preload

CMD flask run -h 0.0.0.0 -p 5000
