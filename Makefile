# Copyright (C) 2011 Manuel Munz <freifunk at somakoma de>
# This is free software, licensed under the Apache 2.0 license.

include $(TOPDIR)/rules.mk

PKG_NAME:=CyberWrt
PKG_RELEASE:=2

PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)

include $(INCLUDE_DIR)/package.mk

define Package/CyberWrt
  SECTION:=base
  CATEGORY:=VyberWrt
  TITLE:=CyberWrt
endef

define Package/CyberWrt/description
CyberWrt
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
endef

define Build/Configure
endef

define Build/Compile
endef

define Package/CyberWrt/install
	$(CP) ./files/* $(1)/
endef

$(eval $(call BuildPackage,CyberWrt))
