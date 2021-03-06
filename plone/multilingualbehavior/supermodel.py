try:
    from plone.supermodel.interfaces import IFieldMetadataHandler
    HAVE_SUPERMODEL = True
except ImportError:
    HAVE_SUPERMODEL = False

if HAVE_SUPERMODEL:
    
    from zope.interface import implements, alsoProvides
    from plone.supermodel.utils import ns
    from plone.multilingualbehavior.interfaces import ILanguageIndependentField
    
    class LanguageIndependentFieldMetadataHandler(object):
        """Define the ``lingua`` namespace.
        
        This lets you write lingua:independent="true" on a field to mark it as
        a language independent field.
        """
        
        implements(IFieldMetadataHandler)
        
        namespace = "http://namespaces.plone.org/supermodel/lingua"
        prefix = "lingua"
    
        def read(self, fieldNode, schema, field):
            independent = fieldNode.get(ns('independent',  self.namespace))
            if independent is not None and independent.lower() in ("true", "on", "yes", "y", "1"):
                alsoProvides(field, ILanguageIndependentField)
    
        def write(self, fieldNode, schema, field):
            if ILanguageIndependentField.providedBy(field):
                fieldNode.set(ns('independent', self.namespace), "true")
