FROM public.ecr.aws/lambda/python@sha256:d81866a7ab07fb9e725dd4610076462f6eb3b86f2ff771f41bd123127eed6976 as build
RUN yum install -y unzip && \
    curl -Lo "/tmp/chromedriver.zip" "https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip" && \
    curl -Lo "/tmp/chrome-linux.zip" "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F1047731%2Fchrome-linux.zip?alt=media" && \
    unzip /tmp/chromedriver.zip -d /opt/ && \
    unzip /tmp/chrome-linux.zip -d /opt/

FROM public.ecr.aws/lambda/python@sha256:d81866a7ab07fb9e725dd4610076462f6eb3b86f2ff771f41bd123127eed6976
RUN yum install atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY --from=build /opt/chrome-linux /opt/chrome
COPY --from=build /opt/chromedriver /opt/
COPY ./src ./src
