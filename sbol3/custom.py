import rdflib

from . import *


class CustomIdentified(Identified):

    def __init__(self, type_uri: str = None, *, identity: str = None,
                 sbol_type_uri: str = SBOL_IDENTIFIED) -> None:
        super().__init__(identity, type_uri)
        self.rdf_type = URIProperty(self, rdflib.RDF.type, 1, 1,
                                    initial_value=sbol_type_uri)

    def validate(self, report: ValidationReport = None) -> ValidationReport:
        report = super().validate(report)
        if self.rdf_type is None:
            message = 'rdf_type is a required property of CustomIdentified'
            report.addError(None, message)
        return report


class CustomTopLevel(TopLevel):

    def __init__(self, identity: str = None, type_uri: str = None,
                 *, sbol_type_uri: str = SBOL_TOP_LEVEL) -> None:
        super().__init__(identity, type_uri)
        self.rdf_type = URIProperty(self, rdflib.RDF.type, 1, 1,
                                    initial_value=sbol_type_uri)

    def validate(self, report: ValidationReport = None) -> ValidationReport:
        report = super().validate(report)
        if self.rdf_type is None:
            message = 'rdf_type is a required property of CustomTopLevel'
            report.addError(None, message)
        return report
