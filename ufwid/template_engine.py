
from abc import ABCMeta, abstractmethod, abstractproperty


class TemplateEngine(six.metaclass(ABCMeta)):

	@abstractmethod
	def render(self, template):
		pass

	@abstractmethod
	def parse(self, template):
		pass

	def _parse_element(self, element):
		pass

	def _get_element_paremetrs(self, element):
		pass

	# Template example
	# <body>