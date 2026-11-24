FROM nginx:1.27-alpine

# Statická PWA, nginx počúva na 0.0.0.0:80 (definované v nginx.conf)
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -q --spider http://127.0.0.1/ || exit 1
