from nicegui import ui



def details(row):
	print(row.id)
	print(row)

	# NOW ADD STYLE COLOR RED IN YOU SELECTED LABEL
	row.style("color:red")
	# PRINT TEXT
	print(row.default_slot.children[0].text)

	# NOW UPDATE YOU SELECTED LABEL TO NEW UPDATE TEXT
	row.default_slot.children[0].text = name.value

	# NOW UPDATE
	row.update()



def youremove(row):
	# FOR REMOVE YOU SELECTED USE FUCNTION REMOVE
	my_tasks.remove(row)
	my_tasks.update()



def addnow():
	# NOW APPEND TO my_tasks
	with my_tasks:
		with ui.row() as myrow:
			ui.label(name.value)
			ui.button("update",on_click=lambda:details(myrow))
			ui.button(on_click=lambda:youremove(myrow)).props("flat icon=delete color=red")



name = ui.input(label="you user")
ui.button("add ",on_click=addnow)
my_tasks = ui.column()

ui.run()