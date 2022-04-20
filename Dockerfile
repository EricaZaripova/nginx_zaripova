FROM nginx

RUN mkdir -p ./etc/nginx/sites-enable
COPY nginx/sites/newflaskapp.conf ./etc/nginx/sites-available/newflaskapp.conf
COPY nginx/sites/newfastapiapp.conf ./etc/nginx/sites-available/newfastapiapp.conf

COPY nginx/sites/newflaskapp.conf ./etc/nginx/sites-enable/newflaskapp.conf
COPY nginx/sites/newfastapiapp.conf ./etc/nginx/sites-enable/newfastapiapp.conf

RUN rm ./etc/nginx/conf.d/default.conf
COPY ./nginx/configuration/nginx.conf ./etc/nginx/nginx.conf

COPY ./nginx/images /etc/nginx/images/