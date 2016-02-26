import sublime, sublime_plugin
import webbrowser

class PyrecoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()
		url = "http://127.0.0.1/?tag="
		for region in sel:
			sel_text = self.view.substr(region)
			url += sel_text + ";"
		print(url)
		webbrowser.open_new_tab(url)
