From rakaim/pytesseract

WORKDIR /app
COPY . /app
CMD cp ./data/chi_sim.traineddata /usr/share/tesseract-ocr/4.00/tessdata

RUN pip3 install -r /app/requirments.txt -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
CMD flask initdb

# CMD flask run -h 0.0.0.0 -p 5000
CMD gunicorn -w 3 -b 0.0.0.0:5000 app:app
