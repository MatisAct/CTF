<?xml version="1.0" encoding="UTF-8"?>
  function xsl_myF4b_DOMFrag() {
    $dom = new DOMDocument;
    $tmp = $dom->createDocumentFragment();
    $tmp->appendXML(' <t> foo <tt val="123"/> bar </t> TEST'); 
    return $tmp;
  }
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
     xmlns:php="http://php.net/xsl" exclude-result-prefixes="php">
  <xsl:template match="/">
     PHP xsl_myF4b()=<xsl:copy-of select="php:function('xsl_myF4b_DOMFrag')/node()" />
  </xsl:template>
</xsl:stylesheet>
