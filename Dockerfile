FROM python:3.10-slim
WORKDIR /
#RUN pip install <dependencies>
ADD generate_fwf.py parse_fwf_to_csv.py specs.txt sample_data.json ./
CMD ["python", "./generate_fwf.py"]