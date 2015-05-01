# ensure that PyGTK 2.0 is loaded - not an older version
import pygtk
pygtk.require('2.0')
# import the GTK module
import gtk


class MyGUI:

    def __init__( self, title):
        self.window = gtk.Window()
        self.title = title
        self.window.set_title( title)
        self.window.set_size_request( 300, 200)
        self.window.connect( "destroy", self.destroy)
        self.create_interior()
        self.window.show_all()
        
    def create_interior( self):
        self.mainbox = gtk.VBox()
        self.window.add( self.mainbox)
        # defining statusbar
        self.status_bar = gtk.Statusbar()   
        self.status_bar.show()
        # resize grip - small area in lower right corner for window resizing
        self.status_bar.set_has_resize_grip( False)
        # context identifier
        self.context_id = self.status_bar.get_context_id( "Statusbar example")
        # push() method pushes a new message with the specified context_id
        # onto a statusbar's stack 
        self.status_bar.push( self.context_id, "Welcome to menu!")
        # menu
        label_menu = gtk.Menu()
        load_file_item = gtk.MenuItem( "Load file")
        load_file_item.connect( "activate", self.load_file, self.context_id)
        load_file_item.show()
        undo_item = gtk.MenuItem( "Undo")
        undo_item.connect( "activate", self.undo,self.context_id)
        undo_item.show()
        run_item = gtk.MenuItem( "Run program")
        run_item.connect( "activate", self.run_function, self.context_id)
        run_item.show()
        label_menu.append( load_file_item)
        label_menu.append( undo_item)
        label_menu.append( run_item)
        # menu bar
        self.menu_bar = gtk.MenuBar()
        label_menu_item = gtk.MenuItem( "File")
        label_menu_item.set_submenu( label_menu)
        self.menu_bar.append( label_menu_item)
        self.menu_bar.show()
        self.empty_box=gtk.VBox()
        # packing
        self.mainbox.pack_start( self.menu_bar, expand=False, fill=False)
        self.mainbox.pack_start(self.empty_box)
        self.mainbox.pack_start( self.status_bar, expand=False)
        self.mainbox.show()
    
    def main( self):
        gtk.main()
    
    def destroy( self, w):
        gtk.main_quit()
        
    def load_file( self, w, data):
        self.status_bar.push( data, "Choose a file!")
        d = gtk.FileChooserDialog( title="Load a file",
                               parent=self.window,
                               action=gtk.FILE_CHOOSER_ACTION_OPEN,
                               buttons=("OK",True,"Cancel",False)
                               )
        ok = d.run()
        if ok:
            fullname = d.get_filename()
            self.status_bar.push( data, fullname)
        else:
            self.status_bar.push( data, "File dialog has been canceled.")
        d.destroy()

    def run_function( self, w, data):
        value = "This is some text from run_function."
        self.status_bar.push( data, value)
        
    def undo( self, w, data):
        # pop() method removes the top message with the specified
        # context_id from the statusbar's stack.
        self.status_bar.pop( data)
        
if __name__ == "__main__":
    m = MyGUI( "Statusbar example" )
    m.main()
    
    
    

