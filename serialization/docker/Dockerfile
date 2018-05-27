FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV PACKAGES_ROOT=/packages

RUN apt-get update && apt-get -y install vim-nox build-essential git cmake cmake-curses-gui time astyle pkg-config
RUN git config --global http.sslverify false

RUN git clone --branch release-1.8.0 https://github.com/google/googletest $PACKAGES_ROOT/googletest \
    && mkdir -p $PACKAGES_ROOT/googletest-build \
    && cd $PACKAGES_ROOT/googletest-build \
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=$PACKAGES_ROOT/googletest-install -DBUILD_GTEST=ON ../googletest/ && make -j4 && make install \
    && rm -rf $PACKAGES_ROOT/googletest-build

RUN git clone --branch v1.4.1 https://github.com/google/benchmark.git $PACKAGES_ROOT/benchmark \
    && mkdir -p $PACKAGES_ROOT/benchmark-build \
    && cd $PACKAGES_ROOT/benchmark-build \
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=$PACKAGES_ROOT/benchmark-install -DCMAKE_BUILD_TYPE=RELEASE -DBENCHMARK_ENABLE_TESTING=OFF ../benchmark/ && make -j4 && make install \
    && rm -rf $PACKAGES_ROOT/benchmark-build

RUN git clone --branch v4.2.5 https://github.com/zeromq/libzmq.git $PACKAGES_ROOT/libzmq \
    && mkdir -p $PACKAGES_ROOT/libzmq-build \
    && cd $PACKAGES_ROOT/libzmq-build \
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=$PACKAGES_ROOT/libzmq-install -DBUILD_TESTS=OFF -DBUILD_SHARED_LIBS=OFF ../libzmq/ && make -j4 && make install \
    && rm -rf $PACKAGES_ROOT/libzmq-build

RUN git clone --branch yaml-cpp-0.6.2 https://github.com/jbeder/yaml-cpp.git $PACKAGES_ROOT/yaml-cpp \
    && mkdir -p $PACKAGES_ROOT/yaml-cpp-build \
    && cd $PACKAGES_ROOT/yaml-cpp-build \
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=$PACKAGES_ROOT/yaml-cpp-install -DYAML_CPP_BUILD_TESTS=OFF -DYAML_CPP_BUILD_TOOLS=OFF -DBUILD_SHARED_LIBS=OFF -DYAML_CPP_BUILD_CONTRIB=OFF ../yaml-cpp/ && make -j4 && make install \
    && rm -rf $PACKAGES_ROOT/yaml-cpp-build

RUN git clone --branch v3.5.1 https://github.com/google/protobuf $PACKAGES_ROOT/protobuf \
    && mkdir -p $PACKAGES_ROOT/protobuf-build \
    && cd $PACKAGES_ROOT/protobuf-build \
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=$PACKAGES_ROOT/protobuf-install -Dprotobuf_BUILD_TESTS=OFF  ../protobuf/cmake/ && make -j4 && make install \
    && rm -rf $PACKAGES_ROOT/protobuf-build

RUN git clone --branch v0.6.1 https://github.com/capnproto/capnproto.git $PACKAGES_ROOT/capnproto \
    && mkdir -p $PACKAGES_ROOT/capnproto-build \
    && cd $PACKAGES_ROOT/capnproto-build \
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=$PACKAGES_ROOT/capnproto-install -DBUILD_TESTING=OFF ../capnproto/c++/ && make -j4 && make install \
    && rm -rf $PACKAGES_ROOT/capnproto-build

RUN git clone --branch v1.2.1 https://github.com/eclipse/paho.mqtt.c.git $PACKAGES_ROOT/paho.mqtt.c \
    && mkdir -p $PACKAGES_ROOT/paho.mqtt.c-build \
    && cd $PACKAGES_ROOT/paho.mqtt.c-build \
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=$PACKAGES_ROOT/paho.mqtt.c-install -DBUILD_TESTS=OFF -DBUILD_SHARED_LIBS=OFF ../paho.mqtt.c/ && make -j4 && make install \
    && rm -rf $PACKAGES_ROOT/paho.mqtt.c-build

ADD https://www.sqlite.org/2018/sqlite-autoconf-3230100.tar.gz /tmp/

RUN cd /tmp \
    && tar -xvzf /tmp/sqlite-autoconf-3230100.tar.gz \
    && cd /tmp/sqlite-autoconf-3230100 \
    && ./configure --prefix=$PACKAGES_ROOT/sqlite3 \
    && make -j4 \
    && make install \
    && rm -rf /tmp/sqlite-autoconf-3230100*

CMD [ "/bin/bash" ]
