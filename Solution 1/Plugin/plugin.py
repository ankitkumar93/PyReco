import sublime, sublime_plugin
import webbrowser
import re

class PyrecoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()
		url = "http://127.0.0.1:8080/?tag="
		
		#extract keyword(s) selected
		for region in sel:
			sel_text = self.view.substr(region)
			url += sel_text + ";"
		
		url += "&text="

		#extract background text
		backgroundtext = self.view.substr(sublime.Region(0, self.view.size()))
		textsplit = backgroundtext.split()
		wordlist = ""
		for word in textsplit:
			if re.search('[a-zA-Z]', word):
				filtered_word = re.sub(r'[^A-Za-z0-9. ]+',' ',word)
				shortlist = filtered_word.split()
				for smallword in shortlist:
					if re.search('[a-zA-Z]', smallword):
						wordlist += smallword + ","

		url += str(wordlist)

		webbrowser.open_new_tab(url)
