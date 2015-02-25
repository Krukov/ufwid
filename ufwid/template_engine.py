
from abc import ABCMeta, abstractmethod, abstractproperty


from lxml import etree

import urwid
import six


class BaseTemplate(six.add_metaclass(ABCMeta)):
	 
	def __init__(self, template):
		self._template = template

	@abstractmethod
	def render(self):
		for element in self._get_iter_elements():
			self._parse_element(element)

	@abstractmethod
	def _parse_element(self, element):
		pass

	@abstractmethod
	def _get_element_paremetrs(self, element):
		pass


class Element(six.add_metaclass(ABCMeta))
	
	proxy = urwid.Button

	def __init__(self, obj):
		self.element = obj

class Button(Element):
	
	

class HtmlTemplate(BaseTemplate):
	_map = {
		'button': (urwid.Button, {'label': 'text', }), 
		'a': urwid.Button, 
		'dev': None, 
		'form': None,
	}

	def render(self):
		template = etree.fromstring(self._template)


	def _parse_element(self, element):

