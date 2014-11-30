from gi.repository import Gtk

class MyExample(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("delete-event", Gtk.main_quit)

        liststore = Gtk.ListStore(str)
        for match in ["test1", "test2", "test3", "spam", "foo", "eggs", "bar"]:
            liststore.append([match])

        completion = Gtk.EntryCompletion()
        completion.set_model(liststore)
        completion.set_text_column(0)

        entry = Gtk.Entry()
        entry.set_completion(completion)
        self.add(entry)
        self.show_all()

if __name__ == "__main__":
    app = MyExample()
    Gtk.main()