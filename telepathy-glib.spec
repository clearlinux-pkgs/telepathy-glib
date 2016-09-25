#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : telepathy-glib
Version  : 0.24.1
Release  : 3
URL      : https://telepathy.freedesktop.org/releases/telepathy-glib/telepathy-glib-0.24.1.tar.gz
Source0  : https://telepathy.freedesktop.org/releases/telepathy-glib/telepathy-glib-0.24.1.tar.gz
Summary  : GLib utility library for the Telepathy framework
Group    : Development/Tools
License  : LGPL-2.1
Requires: telepathy-glib-lib
Requires: telepathy-glib-data
Requires: telepathy-glib-doc
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)

%description
==============
telepathy-glib
==============
This is a library for GLib-based Telepathy components.

%package data
Summary: data components for the telepathy-glib package.
Group: Data

%description data
data components for the telepathy-glib package.


%package dev
Summary: dev components for the telepathy-glib package.
Group: Development
Requires: telepathy-glib-lib
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
%setup -q -n telepathy-glib-0.24.1

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

%files data
%defattr(-,root,root,-)
/usr/share/gir-1.0/TelepathyGLib-0.12.gir

%files dev
%defattr(-,root,root,-)
/usr/include/telepathy-1.0/telepathy-glib/_gen/error-str.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/genums.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/gtypes.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/telepathy-enums.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/telepathy-interfaces.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-account-manager.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-account.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-call-content-media-description.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-call-content.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-call-stream-endpoint.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-call-stream.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-channel-dispatch-operation.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-channel-dispatcher.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-channel-request.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-channel.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-client.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-connection-manager.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-connection.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-dbus-daemon.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-debug.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-generic.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-media-session-handler.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-media-stream-handler.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-protocol.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-cli-tls-cert.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-account-manager.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-account.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-call-content-media-description.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-call-content.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-call-stream-endpoint.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-call-stream.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-channel-dispatch-operation.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-channel-dispatcher.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-channel-request.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-channel.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-client.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-connection-manager.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-connection.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-debug.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-generic.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-media-session-handler.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-media-stream-handler.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-protocol.h
/usr/include/telepathy-1.0/telepathy-glib/_gen/tp-svc-tls-cert.h
/usr/include/telepathy-1.0/telepathy-glib/account-channel-request.h
/usr/include/telepathy-1.0/telepathy-glib/account-manager.h
/usr/include/telepathy-1.0/telepathy-glib/account-request.h
/usr/include/telepathy-1.0/telepathy-glib/account.h
/usr/include/telepathy-1.0/telepathy-glib/add-dispatch-operation-context.h
/usr/include/telepathy-1.0/telepathy-glib/automatic-client-factory.h
/usr/include/telepathy-1.0/telepathy-glib/automatic-proxy-factory.h
/usr/include/telepathy-1.0/telepathy-glib/base-call-channel.h
/usr/include/telepathy-1.0/telepathy-glib/base-call-content.h
/usr/include/telepathy-1.0/telepathy-glib/base-call-stream.h
/usr/include/telepathy-1.0/telepathy-glib/base-channel.h
/usr/include/telepathy-1.0/telepathy-glib/base-client.h
/usr/include/telepathy-1.0/telepathy-glib/base-connection-manager.h
/usr/include/telepathy-1.0/telepathy-glib/base-connection.h
/usr/include/telepathy-1.0/telepathy-glib/base-contact-list.h
/usr/include/telepathy-1.0/telepathy-glib/base-media-call-channel.h
/usr/include/telepathy-1.0/telepathy-glib/base-media-call-content.h
/usr/include/telepathy-1.0/telepathy-glib/base-media-call-stream.h
/usr/include/telepathy-1.0/telepathy-glib/base-password-channel.h
/usr/include/telepathy-1.0/telepathy-glib/base-protocol.h
/usr/include/telepathy-1.0/telepathy-glib/base-room-config.h
/usr/include/telepathy-1.0/telepathy-glib/basic-proxy-factory.h
/usr/include/telepathy-1.0/telepathy-glib/call-channel.h
/usr/include/telepathy-1.0/telepathy-glib/call-content-media-description.h
/usr/include/telepathy-1.0/telepathy-glib/call-content.h
/usr/include/telepathy-1.0/telepathy-glib/call-misc.h
/usr/include/telepathy-1.0/telepathy-glib/call-stream-endpoint.h
/usr/include/telepathy-1.0/telepathy-glib/call-stream.h
/usr/include/telepathy-1.0/telepathy-glib/capabilities.h
/usr/include/telepathy-1.0/telepathy-glib/channel-dispatch-operation.h
/usr/include/telepathy-1.0/telepathy-glib/channel-dispatcher.h
/usr/include/telepathy-1.0/telepathy-glib/channel-factory-iface.h
/usr/include/telepathy-1.0/telepathy-glib/channel-iface.h
/usr/include/telepathy-1.0/telepathy-glib/channel-manager.h
/usr/include/telepathy-1.0/telepathy-glib/channel-request.h
/usr/include/telepathy-1.0/telepathy-glib/channel.h
/usr/include/telepathy-1.0/telepathy-glib/client-channel-factory.h
/usr/include/telepathy-1.0/telepathy-glib/client-message.h
/usr/include/telepathy-1.0/telepathy-glib/client.h
/usr/include/telepathy-1.0/telepathy-glib/cm-message.h
/usr/include/telepathy-1.0/telepathy-glib/connection-contact-list.h
/usr/include/telepathy-1.0/telepathy-glib/connection-manager.h
/usr/include/telepathy-1.0/telepathy-glib/connection.h
/usr/include/telepathy-1.0/telepathy-glib/contact-operations.h
/usr/include/telepathy-1.0/telepathy-glib/contact-search-result.h
/usr/include/telepathy-1.0/telepathy-glib/contact-search.h
/usr/include/telepathy-1.0/telepathy-glib/contact.h
/usr/include/telepathy-1.0/telepathy-glib/contacts-mixin.h
/usr/include/telepathy-1.0/telepathy-glib/dbus-daemon.h
/usr/include/telepathy-1.0/telepathy-glib/dbus-properties-mixin.h
/usr/include/telepathy-1.0/telepathy-glib/dbus-tube-channel.h
/usr/include/telepathy-1.0/telepathy-glib/dbus.h
/usr/include/telepathy-1.0/telepathy-glib/debug-ansi.h
/usr/include/telepathy-1.0/telepathy-glib/debug-client.h
/usr/include/telepathy-1.0/telepathy-glib/debug-message.h
/usr/include/telepathy-1.0/telepathy-glib/debug-sender.h
/usr/include/telepathy-1.0/telepathy-glib/debug.h
/usr/include/telepathy-1.0/telepathy-glib/defs.h
/usr/include/telepathy-1.0/telepathy-glib/dtmf.h
/usr/include/telepathy-1.0/telepathy-glib/enums.h
/usr/include/telepathy-1.0/telepathy-glib/errors.h
/usr/include/telepathy-1.0/telepathy-glib/exportable-channel.h
/usr/include/telepathy-1.0/telepathy-glib/file-transfer-channel.h
/usr/include/telepathy-1.0/telepathy-glib/gnio-util.h
/usr/include/telepathy-1.0/telepathy-glib/group-mixin.h
/usr/include/telepathy-1.0/telepathy-glib/gtypes.h
/usr/include/telepathy-1.0/telepathy-glib/handle-channels-context.h
/usr/include/telepathy-1.0/telepathy-glib/handle-repo-dynamic.h
/usr/include/telepathy-1.0/telepathy-glib/handle-repo-static.h
/usr/include/telepathy-1.0/telepathy-glib/handle-repo.h
/usr/include/telepathy-1.0/telepathy-glib/handle.h
/usr/include/telepathy-1.0/telepathy-glib/heap.h
/usr/include/telepathy-1.0/telepathy-glib/interfaces.h
/usr/include/telepathy-1.0/telepathy-glib/intset.h
/usr/include/telepathy-1.0/telepathy-glib/media-interfaces.h
/usr/include/telepathy-1.0/telepathy-glib/message-mixin.h
/usr/include/telepathy-1.0/telepathy-glib/message.h
/usr/include/telepathy-1.0/telepathy-glib/observe-channels-context.h
/usr/include/telepathy-1.0/telepathy-glib/presence-mixin.h
/usr/include/telepathy-1.0/telepathy-glib/properties-mixin.h
/usr/include/telepathy-1.0/telepathy-glib/protocol.h
/usr/include/telepathy-1.0/telepathy-glib/proxy-subclass.h
/usr/include/telepathy-1.0/telepathy-glib/proxy.h
/usr/include/telepathy-1.0/telepathy-glib/room-info.h
/usr/include/telepathy-1.0/telepathy-glib/room-list.h
/usr/include/telepathy-1.0/telepathy-glib/run.h
/usr/include/telepathy-1.0/telepathy-glib/signalled-message.h
/usr/include/telepathy-1.0/telepathy-glib/simple-approver.h
/usr/include/telepathy-1.0/telepathy-glib/simple-client-factory.h
/usr/include/telepathy-1.0/telepathy-glib/simple-handler.h
/usr/include/telepathy-1.0/telepathy-glib/simple-observer.h
/usr/include/telepathy-1.0/telepathy-glib/simple-password-manager.h
/usr/include/telepathy-1.0/telepathy-glib/stream-tube-channel.h
/usr/include/telepathy-1.0/telepathy-glib/stream-tube-connection.h
/usr/include/telepathy-1.0/telepathy-glib/svc-account-manager.h
/usr/include/telepathy-1.0/telepathy-glib/svc-account.h
/usr/include/telepathy-1.0/telepathy-glib/svc-call.h
/usr/include/telepathy-1.0/telepathy-glib/svc-channel-dispatch-operation.h
/usr/include/telepathy-1.0/telepathy-glib/svc-channel-dispatcher.h
/usr/include/telepathy-1.0/telepathy-glib/svc-channel-request.h
/usr/include/telepathy-1.0/telepathy-glib/svc-channel.h
/usr/include/telepathy-1.0/telepathy-glib/svc-client.h
/usr/include/telepathy-1.0/telepathy-glib/svc-connection-manager.h
/usr/include/telepathy-1.0/telepathy-glib/svc-connection.h
/usr/include/telepathy-1.0/telepathy-glib/svc-debug.h
/usr/include/telepathy-1.0/telepathy-glib/svc-generic.h
/usr/include/telepathy-1.0/telepathy-glib/svc-media-interfaces.h
/usr/include/telepathy-1.0/telepathy-glib/svc-properties-interface.h
/usr/include/telepathy-1.0/telepathy-glib/svc-protocol.h
/usr/include/telepathy-1.0/telepathy-glib/svc-tls.h
/usr/include/telepathy-1.0/telepathy-glib/telepathy-glib-dbus.h
/usr/include/telepathy-1.0/telepathy-glib/telepathy-glib.h
/usr/include/telepathy-1.0/telepathy-glib/text-channel.h
/usr/include/telepathy-1.0/telepathy-glib/text-mixin.h
/usr/include/telepathy-1.0/telepathy-glib/tls-certificate-rejection.h
/usr/include/telepathy-1.0/telepathy-glib/tls-certificate.h
/usr/include/telepathy-1.0/telepathy-glib/util.h
/usr/include/telepathy-1.0/telepathy-glib/variant-util.h
/usr/include/telepathy-1.0/telepathy-glib/verify.h
/usr/include/telepathy-1.0/telepathy-glib/version.h
/usr/lib64/*.so
/usr/lib64/girepository-1.0/TelepathyGLib-0.12.typelib
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/telepathy-glib/TpBaseCallChannel.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseCallContent.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseCallStream.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseChannel.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseConnection.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseConnectionManager.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseMediaCallChannel.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseMediaCallContent.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseMediaCallStream.html
/usr/share/gtk-doc/html/telepathy-glib/TpBaseRoomConfig.html
/usr/share/gtk-doc/html/telepathy-glib/TpCMMessage.html
/usr/share/gtk-doc/html/telepathy-glib/TpCallContentMediaDescription.html
/usr/share/gtk-doc/html/telepathy-glib/TpCallStreamEndpoint.html
/usr/share/gtk-doc/html/telepathy-glib/TpChannelFactoryIface.html
/usr/share/gtk-doc/html/telepathy-glib/TpChannelIface.html
/usr/share/gtk-doc/html/telepathy-glib/TpChannelManager.html
/usr/share/gtk-doc/html/telepathy-glib/TpClientMessage.html
/usr/share/gtk-doc/html/telepathy-glib/TpDebugClient.html
/usr/share/gtk-doc/html/telepathy-glib/TpDebugMessage.html
/usr/share/gtk-doc/html/telepathy-glib/TpDynamicHandleRepo.html
/usr/share/gtk-doc/html/telepathy-glib/TpExportableChannel.html
/usr/share/gtk-doc/html/telepathy-glib/TpIntset.html
/usr/share/gtk-doc/html/telepathy-glib/TpMessage.html
/usr/share/gtk-doc/html/telepathy-glib/TpSignalledMessage.html
/usr/share/gtk-doc/html/telepathy-glib/TpStaticHandleRepo.html
/usr/share/gtk-doc/html/telepathy-glib/TpTLSCertificate.html
/usr/share/gtk-doc/html/telepathy-glib/TpTLSCertificateRejection.html
/usr/share/gtk-doc/html/telepathy-glib/annotation-glossary.html
/usr/share/gtk-doc/html/telepathy-glib/ch-client.html
/usr/share/gtk-doc/html/telepathy-glib/ch-dbus.html
/usr/share/gtk-doc/html/telepathy-glib/ch-obsolete.html
/usr/share/gtk-doc/html/telepathy-glib/ch-protocol.html
/usr/share/gtk-doc/html/telepathy-glib/ch-service-base.html
/usr/share/gtk-doc/html/telepathy-glib/ch-service-dbus.html
/usr/share/gtk-doc/html/telepathy-glib/ch-service-handles.html
/usr/share/gtk-doc/html/telepathy-glib/ch-utilities.html
/usr/share/gtk-doc/html/telepathy-glib/home.png
/usr/share/gtk-doc/html/telepathy-glib/index.html
/usr/share/gtk-doc/html/telepathy-glib/index.sgml
/usr/share/gtk-doc/html/telepathy-glib/left.png
/usr/share/gtk-doc/html/telepathy-glib/right.png
/usr/share/gtk-doc/html/telepathy-glib/style.css
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-TpContactsMixin.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-TpGroupMixin.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-TpHeap.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-TpMessageMixin.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-TpPresenceMixin.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-TpPropertiesMixin.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-TpTextMixin.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-account-channel-request.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-account-manager.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-account-request.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-account.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-add-dispatch-operation-context.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-asv.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-automatic-client-factory.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-automatic-proxy-factory.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-base-client.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-base-contact-list.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-base-password-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-base-protocol.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-basic-proxy-factory.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-call-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-call-content.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-call-misc.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-call-stream.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-capabilities.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-auth.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-contactsearch.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-dispatch-operation.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-dispatcher.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-file-transfer.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-group.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-media.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-request.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-room.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-roomlist.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-text.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-tube.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel-tubes.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-cli-anonymity.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-cli-call-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-cli-call-content.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-cli-call-misc.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-cli-call-stream.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-cli-service-point.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-client-channel-factory.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-client.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-addressing.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-aliasing.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-avatars.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-balance.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-caps.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-cellular.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-client-types.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-contact-info.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-contact-list.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-contacts.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-location.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-mail.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-manager.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-powersaving.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-presence.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-renaming.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-requests.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-sidecars.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection-simple-presence.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-connection.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-contact-search-result.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-contact-search.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-contact.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-dbus-properties-mixin.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-dbus-tube-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-dbus.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-debug-ansi.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-debug-sender.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-debug.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-defs.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-dtmf.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-enums.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-errors.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-file-transfer-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-gnio-util.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-gtypes.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-handle-channels-context.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-handle-repo.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-handle.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-interfaces.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-media-interfaces.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-observe-channels-context.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-protocol.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-proxy-dbus-core.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-proxy-subclass.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-proxy-tp-properties.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-proxy.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-room-info.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-room-list.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-run.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-simple-approver.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-simple-client-factory.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-simple-handler.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-simple-observer.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-simple-password-manager.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-stream-tube-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-stream-tube-connection.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-account-manager.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-account.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-anonymity.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-auth.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-call.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-contactlist.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-contactsearch.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-dispatch-operation.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-dispatcher.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-file-transfer.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-ft-metadata.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-group.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-media.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-request.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-room.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-roomlist.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-securable.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-text.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-tube.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel-tubes.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-client.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-connection-manager.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-connection.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-debug.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-generic.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-media-interfaces.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-protocol.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-service-point.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc-tls.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-svc.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-text-channel.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-util.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-vardict.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-variant-util.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib-version.html
/usr/share/gtk-doc/html/telepathy-glib/telepathy-glib.devhelp2
/usr/share/gtk-doc/html/telepathy-glib/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
