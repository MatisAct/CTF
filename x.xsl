<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
     xmlns:php="http://php.net/xsl" exclude-result-prefixes="php">
 <xsl:template match="/">
	PHP time()=<xsl:value-of select="php:function('var_dump',<xsl:value-of select="php:function('scandir','.')" />)" />, 
  </xsl:template>
</xsl:stylesheet>
