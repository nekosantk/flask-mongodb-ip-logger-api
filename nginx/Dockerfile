FROM nginx

RUN mkdir /etc/nginx/templates
COPY default.conf.template /etc/nginx/templates
COPY /ssl /
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]