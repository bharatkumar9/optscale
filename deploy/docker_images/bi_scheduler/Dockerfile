FROM acura-dr.dts.loc/optscale_python:94098b67b949e2fabcc2404becf90a25f77496e6

WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scheduler.py ./

CMD ["python3", "/src/scheduler.py"]
