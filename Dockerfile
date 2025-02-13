# We're using Ubuntu 20.10
FROM ximfine/xproject:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b x-sql-extended https://github.com/ximfine/XBot-Remix /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

#
# Make open port TCP
#
EXPOSE 80 443 8443

# Upgrade pip
RUN pip install --upgrade pip

#Install python requirements
# RUN pip3 install -r https://raw.githubusercontent.com/ximfine/XBot-Remix/x-sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
