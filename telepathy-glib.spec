#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : telepathy-glib
Version  : 0.99.11
Release  : 2
URL      : https://telepathy.freedesktop.org/releases/telepathy-glib/telepathy-glib-0.99.11.tar.gz
Source0  : https://telepathy.freedesktop.org/releases/telepathy-glib/telepathy-glib-0.99.11.tar.gz
Summary  : Access to Telepathy logs
Group    : Development/Tools
License  : LGPL-2.1
Requires: telepathy-glib-lib
Requires: telepathy-glib-bin
Requires: telepathy-glib-data
Requires: telepathy-glib-doc
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(sqlite3)

%description
==============
telepathy-glib
==============
Telepathy is a D-Bus framework for unifying real time communication,
including instant messaging, voice calls and video calls. It abstracts
differences between protocols to provide a unified interface for
applications.

%package bin
Summary: bin components for the telepathy-glib package.
Group: Binaries
Requires: telepathy-glib-data

%description bin
bin components for the telepathy-glib package.


%package data
Summary: data components for the telepathy-glib package.
Group: Data

%description data
data components for the telepathy-glib package.


%package dev
Summary: dev components for the telepathy-glib package.
Group: Development
Requires: telepathy-glib-lib
Requires: telepathy-glib-bin
Requires: telepathy-glib-data
Provides: telepathy-glib-devel

%description dev
dev components for the telepathy-glib package.


%package doc
Summary: doc components for the telepathy-glib package.
Group: Documentation

%description doc
doc components for the telepathy-glib package.


%package lib
Summary: lib components for the telepathy-glib package.
Group: Libraries
Requires: telepathy-glib-data

%description lib
lib components for the telepathy-glib package.


%prep
%setup -q -n telepathy-glib-0.99.11

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/telepathy-logger-1

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/im.telepathy.v1.Client.Logger.service
/usr/share/dbus-1/services/im.telepathy.v1.Logger.service
/usr/share/gir-1.0/TelepathyGLib-1.gir
/usr/share/gir-1.0/TelepathyGLibDBus-1.gir
/usr/share/gir-1.0/TelepathyLogger-1.gir
/usr/share/glib-2.0/schemas/im.telepathy.v1.Logger.gschema.xml
/usr/share/telepathy-1/clients/Logger.client

%files dev
%defattr(-,root,root,-)
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/gtypes.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/telepathy-interfaces.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-account-manager.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-account.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-content-media-description.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-content.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-stream-endpoint.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-stream.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel-dispatch-operation.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel-dispatcher.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel-request.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-client.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-connection-manager.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-connection.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-debug.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-generic.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-logger.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-protocol.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-tls-cert.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-account-manager.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-account.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-content-media-description.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-content.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-stream-endpoint.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-stream.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel-dispatch-operation.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel-dispatcher.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel-request.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-client.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-connection-manager.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-connection.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-debug.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-generic.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-logger.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-protocol.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-tls-cert.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/asv.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/cli-call.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/cli-channel.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/cli-connection.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/cli-misc.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/cli-proxy.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/dbus-properties-mixin.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/gnio-util.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/gtypes.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/interfaces.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/sliced-gvalue.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-account-manager.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-account.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-call.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-channel-dispatch-operation.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-channel-dispatcher.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-channel-request.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-channel.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-client.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-connection-manager.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-connection.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-debug.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-generic.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-interface.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-logger.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-properties-interface.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-protocol.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/svc-tls.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/telepathy-glib-dbus.h
/usr/include/telepathy-glib-1-dbus/telepathy-glib/value-array.h
/usr/include/telepathy-glib-1/telepathy-glib/_gen/error-str.h
/usr/include/telepathy-glib-1/telepathy-glib/_gen/genums.h
/usr/include/telepathy-glib-1/telepathy-glib/_gen/telepathy-enums.h
/usr/include/telepathy-glib-1/telepathy-glib/account-channel-request.h
/usr/include/telepathy-glib-1/telepathy-glib/account-manager.h
/usr/include/telepathy-glib-1/telepathy-glib/account-request.h
/usr/include/telepathy-glib-1/telepathy-glib/account.h
/usr/include/telepathy-glib-1/telepathy-glib/add-dispatch-operation-context.h
/usr/include/telepathy-glib-1/telepathy-glib/automatic-client-factory.h
/usr/include/telepathy-glib-1/telepathy-glib/base-call-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/base-call-content.h
/usr/include/telepathy-glib-1/telepathy-glib/base-call-stream.h
/usr/include/telepathy-glib-1/telepathy-glib/base-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/base-client.h
/usr/include/telepathy-glib-1/telepathy-glib/base-connection-manager.h
/usr/include/telepathy-glib-1/telepathy-glib/base-connection.h
/usr/include/telepathy-glib-1/telepathy-glib/base-contact-list.h
/usr/include/telepathy-glib-1/telepathy-glib/base-media-call-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/base-media-call-content.h
/usr/include/telepathy-glib-1/telepathy-glib/base-media-call-stream.h
/usr/include/telepathy-glib-1/telepathy-glib/base-password-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/base-protocol.h
/usr/include/telepathy-glib-1/telepathy-glib/base-room-config.h
/usr/include/telepathy-glib-1/telepathy-glib/call-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/call-content-media-description.h
/usr/include/telepathy-glib-1/telepathy-glib/call-content.h
/usr/include/telepathy-glib-1/telepathy-glib/call-stream-endpoint.h
/usr/include/telepathy-glib-1/telepathy-glib/call-stream.h
/usr/include/telepathy-glib-1/telepathy-glib/capabilities.h
/usr/include/telepathy-glib-1/telepathy-glib/channel-dispatch-operation.h
/usr/include/telepathy-glib-1/telepathy-glib/channel-dispatcher.h
/usr/include/telepathy-glib-1/telepathy-glib/channel-filter.h
/usr/include/telepathy-glib-1/telepathy-glib/channel-manager-request.h
/usr/include/telepathy-glib-1/telepathy-glib/channel-manager.h
/usr/include/telepathy-glib-1/telepathy-glib/channel-request.h
/usr/include/telepathy-glib-1/telepathy-glib/channel.h
/usr/include/telepathy-glib-1/telepathy-glib/client-factory.h
/usr/include/telepathy-glib-1/telepathy-glib/client-message.h
/usr/include/telepathy-glib-1/telepathy-glib/client.h
/usr/include/telepathy-glib-1/telepathy-glib/cm-message.h
/usr/include/telepathy-glib-1/telepathy-glib/connection-contact-list.h
/usr/include/telepathy-glib-1/telepathy-glib/connection-manager.h
/usr/include/telepathy-glib-1/telepathy-glib/connection.h
/usr/include/telepathy-glib-1/telepathy-glib/contact-operations.h
/usr/include/telepathy-glib-1/telepathy-glib/contact-search-result.h
/usr/include/telepathy-glib-1/telepathy-glib/contact-search.h
/usr/include/telepathy-glib-1/telepathy-glib/contact.h
/usr/include/telepathy-glib-1/telepathy-glib/dbus-tube-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/dbus.h
/usr/include/telepathy-glib-1/telepathy-glib/debug-client.h
/usr/include/telepathy-glib-1/telepathy-glib/debug-message.h
/usr/include/telepathy-glib-1/telepathy-glib/debug-sender.h
/usr/include/telepathy-glib-1/telepathy-glib/debug.h
/usr/include/telepathy-glib-1/telepathy-glib/defs.h
/usr/include/telepathy-glib-1/telepathy-glib/dtmf.h
/usr/include/telepathy-glib-1/telepathy-glib/enums.h
/usr/include/telepathy-glib-1/telepathy-glib/errors.h
/usr/include/telepathy-glib-1/telepathy-glib/file-transfer-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/gnio-unix.h
/usr/include/telepathy-glib-1/telepathy-glib/group-mixin.h
/usr/include/telepathy-glib-1/telepathy-glib/handle-channel-context.h
/usr/include/telepathy-glib-1/telepathy-glib/handle-repo-dynamic.h
/usr/include/telepathy-glib-1/telepathy-glib/handle-repo-static.h
/usr/include/telepathy-glib-1/telepathy-glib/handle-repo.h
/usr/include/telepathy-glib-1/telepathy-glib/handle.h
/usr/include/telepathy-glib-1/telepathy-glib/heap.h
/usr/include/telepathy-glib-1/telepathy-glib/intset.h
/usr/include/telepathy-glib-1/telepathy-glib/logger.h
/usr/include/telepathy-glib-1/telepathy-glib/message-mixin.h
/usr/include/telepathy-glib-1/telepathy-glib/message.h
/usr/include/telepathy-glib-1/telepathy-glib/observe-channel-context.h
/usr/include/telepathy-glib-1/telepathy-glib/presence-mixin.h
/usr/include/telepathy-glib-1/telepathy-glib/protocol.h
/usr/include/telepathy-glib-1/telepathy-glib/proxy-subclass.h
/usr/include/telepathy-glib-1/telepathy-glib/proxy.h
/usr/include/telepathy-glib-1/telepathy-glib/room-info.h
/usr/include/telepathy-glib-1/telepathy-glib/room-list.h
/usr/include/telepathy-glib-1/telepathy-glib/run.h
/usr/include/telepathy-glib-1/telepathy-glib/signalled-message.h
/usr/include/telepathy-glib-1/telepathy-glib/simple-approver.h
/usr/include/telepathy-glib-1/telepathy-glib/simple-handler.h
/usr/include/telepathy-glib-1/telepathy-glib/simple-observer.h
/usr/include/telepathy-glib-1/telepathy-glib/simple-password-manager.h
/usr/include/telepathy-glib-1/telepathy-glib/stream-tube-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/stream-tube-connection.h
/usr/include/telepathy-glib-1/telepathy-glib/telepathy-glib.h
/usr/include/telepathy-glib-1/telepathy-glib/text-channel.h
/usr/include/telepathy-glib-1/telepathy-glib/tls-certificate-rejection.h
/usr/include/telepathy-glib-1/telepathy-glib/tls-certificate.h
/usr/include/telepathy-glib-1/telepathy-glib/util.h
/usr/include/telepathy-glib-1/telepathy-glib/variant-util.h
/usr/include/telepathy-glib-1/telepathy-glib/version.h
/usr/include/telepathy-logger-1/telepathy-logger/call-event.h
/usr/include/telepathy-logger-1/telepathy-logger/debug.h
/usr/include/telepathy-logger-1/telepathy-logger/entity.h
/usr/include/telepathy-logger-1/telepathy-logger/event.h
/usr/include/telepathy-logger-1/telepathy-logger/log-manager.h
/usr/include/telepathy-logger-1/telepathy-logger/log-walker.h
/usr/include/telepathy-logger-1/telepathy-logger/telepathy-logger.h
/usr/include/telepathy-logger-1/telepathy-logger/text-event.h
/usr/lib64/*.so
/usr/lib64/girepository-1.0/TelepathyGLib-1.typelib
/usr/lib64/girepository-1.0/TelepathyGLibDBus-1.typelib
/usr/lib64/girepository-1.0/TelepathyLogger-1.typelib
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseCallChannel.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseCallContent.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseCallStream.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseChannel.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseConnection.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseConnectionManager.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseMediaCallChannel.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseMediaCallContent.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseMediaCallStream.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpBaseRoomConfig.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpCMMessage.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpCallContentMediaDescription.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpCallStreamEndpoint.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpChannelManager.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpChannelManagerRequest.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpClientMessage.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpDebugClient.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpDebugMessage.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpDynamicHandleRepo.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpIntset.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpMessage.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpSignalledMessage.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpStaticHandleRepo.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpTLSCertificate.html
/usr/share/gtk-doc/html/telepathy-glib-1/TpTLSCertificateRejection.html
/usr/share/gtk-doc/html/telepathy-glib-1/annotation-glossary.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-cli.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-client.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-codegen.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-dbus.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-protocol.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-service-base.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-service-dbus.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-service-handles.html
/usr/share/gtk-doc/html/telepathy-glib-1/ch-utilities.html
/usr/share/gtk-doc/html/telepathy-glib-1/home.png
/usr/share/gtk-doc/html/telepathy-glib-1/index.html
/usr/share/gtk-doc/html/telepathy-glib-1/index.sgml
/usr/share/gtk-doc/html/telepathy-glib-1/left-insensitive.png
/usr/share/gtk-doc/html/telepathy-glib-1/left.png
/usr/share/gtk-doc/html/telepathy-glib-1/right-insensitive.png
/usr/share/gtk-doc/html/telepathy-glib-1/right.png
/usr/share/gtk-doc/html/telepathy-glib-1/style.css
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-1.devhelp2
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpGroupMixin.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpHeap.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpMessageMixin.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpPresenceMixinInterface.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpSvcInterface.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-account-channel-request.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-account-manager.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-account-request.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-account.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-add-dispatch-operation-context.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-asv.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-automatic-client-factory.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-client.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-contact-list.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-password-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-protocol.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-call-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-call-content.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-call-stream.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-capabilities.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-auth.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-contactsearch.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-dispatch-operation.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-dispatcher.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-file-transfer.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-filter.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-group.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-media.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-request.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-room.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-roomlist.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-text.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-tube.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-account-manager.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-anonymity.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-content.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-misc.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-stream.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-channel-dispatcher.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-client.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-connection-manager.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-connection-protocol-specifics.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-connection.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-service-point.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-client-factory.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-client.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-addressing.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-aliasing.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-avatars.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-balance.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-caps.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-cellular.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-client-types.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-contact-info.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-contact-list.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-location.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-mail.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-manager.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-powersaving.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-presence.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-renaming.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-requests.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-sidecars.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-contact-search-result.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-contact-search.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-contact.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-dbus-properties-mixin.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-dbus-tube-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-dbus.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-debug-sender.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-debug.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-dtmf.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-enums.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-errors.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-file-transfer-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-gnio-util.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-gtypes.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-handle-channel-context.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-handle-repo.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-handle.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-interfaces.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-logger.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-observe-channel-context.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-protocol.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-proxy-dbus-core.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-proxy-subclass.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-proxy.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-room-info.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-room-list.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-run.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-approver.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-handler.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-observer.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-password-manager.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-sliced-gvalue.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-stream-tube-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-stream-tube-connection.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-account-manager.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-account.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-anonymity.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-auth.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-call.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-contactsearch.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-dispatch-operation.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-dispatcher.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-file-transfer.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-ft-metadata.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-group.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-request.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-room.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-roomlist.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-securable.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-text.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-tube.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-client.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-connection-manager.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-connection.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-debug.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-generic.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-logger.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-protocol.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-service-point.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-tls.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-text-channel.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-util.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-value-array.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-vardict.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-variant-util.html
/usr/share/gtk-doc/html/telepathy-glib-1/telepathy-glib-version.html
/usr/share/gtk-doc/html/telepathy-glib-1/up-insensitive.png
/usr/share/gtk-doc/html/telepathy-glib-1/up.png
/usr/share/gtk-doc/html/telepathy-logger-1/TplCallEvent.html
/usr/share/gtk-doc/html/telepathy-logger-1/TplEntity.html
/usr/share/gtk-doc/html/telepathy-logger-1/TplEvent.html
/usr/share/gtk-doc/html/telepathy-logger-1/TplLogManager.html
/usr/share/gtk-doc/html/telepathy-logger-1/TplLogWalker.html
/usr/share/gtk-doc/html/telepathy-logger-1/TplTextEvent.html
/usr/share/gtk-doc/html/telepathy-logger-1/ch-public.html
/usr/share/gtk-doc/html/telepathy-logger-1/home.png
/usr/share/gtk-doc/html/telepathy-logger-1/index.html
/usr/share/gtk-doc/html/telepathy-logger-1/index.sgml
/usr/share/gtk-doc/html/telepathy-logger-1/left-insensitive.png
/usr/share/gtk-doc/html/telepathy-logger-1/left.png
/usr/share/gtk-doc/html/telepathy-logger-1/right-insensitive.png
/usr/share/gtk-doc/html/telepathy-logger-1/right.png
/usr/share/gtk-doc/html/telepathy-logger-1/style.css
/usr/share/gtk-doc/html/telepathy-logger-1/telepathy-logger-1.devhelp2
/usr/share/gtk-doc/html/telepathy-logger-1/up-insensitive.png
/usr/share/gtk-doc/html/telepathy-logger-1/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
