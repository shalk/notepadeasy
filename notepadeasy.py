#python
# -*- coding:gb2312  -*-
import wx
import os

class  MainWindow(wx.Frame):
    def __init__(self,parent,id,title,):
		wx.Frame.__init__(self,parent,id,title,size=(500,300),pos=(500,220))
		self.dirname	= "d:\\"
		self.filename	= "readme.txt"
		self.control	= wx.TextCtrl(self,1,style=wx.TE_MULTILINE)
		self.current    = False
		#-----------menu----------------
		
		menu1	= wx.Menu() #File
 		menu2	= wx.Menu() #Edit
		menu3	= wx.Menu() #Format
		menu4	= wx.Menu() #view
		menu5	= wx.Menu() #help
		
		for id,name,helptext,handler  in \
				[ (wx.ID_OPEN,'打开','打开文件',self.OnOpen),
				  (wx.ID_SAVE,'保存','保存文件',self.OnSave),
				  (wx.ID_SAVEAS,'另存为','另存文件',self.OnSaveAs),
				  (None,None,None,None),
				  (wx.ID_EXIT,'退出','88',self.OnExit)]:
			if id !=None :
				item=menu1.Append(id, tcn(name),tcn(helptext))
				self.Bind(wx.EVT_MENU,handler,item)
			else:
				menu1.AppendSeparator()
		for id,name,helptext,handler  in \
				[ (wx.NewId(),'联系我','by shalk',self.OnContact),
				  (wx.ID_ABOUT,'关于我','by shalk',self.OnAbout)]:
			item=menu5.Append(id, tcn(name),tcn(helptext))
			self.Bind(wx.EVT_MENU,handler,item)
			
		#------------menubar----------
		menubar = wx.MenuBar()
		menubar.Append(menu1,tcn('文件'))
		menubar.Append(menu5,tcn('帮助'))
		self.SetMenuBar(menubar)
		self.CreateStatusBar()
	#--------handler-----------
	def OnOpen(self,event):
		dialog = wx.FileDialog(self,message='Choice a file:',
								defaultDir=self.dirname,
								wildcard='*.*',style=wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
		#	print dialog.GetPath()
			(self.dirname,self.filename)	= os.path.split(dialog.GetPath())
			self.SetTitle(dialog.GetPath()+'- Notepad Easy ')
			textfile 		= open(os.path.join(self.dirname,self.filename),'r')
			self.control.SetValue(textfile.read())
			textfile.close()
			self.current =True
		dialog.Destroy()
		
	def OnSave(self,event):
		if self.current ==False:
			return
		#print "dir:%s#file:%s#" %(self.dirname,self.filename)
		textfile = open(os.path.join(self.dirname,self.filename),'w')
		textfile.write(self.control.GetValue())
		textfile.close()
		
	def OnSaveAs(self,event):
		dialog = wx.FileDialog(self,message='Save as a file:',
								defaultDir=self.dirname,
								defaultFile=self.filename,
								wildcard='*.*',style=wx.SAVE,
								)
		if dialog.ShowModal() ==wx.ID_OK:
			(self.dirname,self.filename)	= os.path.split(dialog.GetPath())
			self.SetTitle(dialog.GetPath()+'- Notepad Easy ')
			self.current =True
			dialog.Destroy()
			self.OnSave(event)
		else:
			dialog.Destroy()
		
	def OnExit(self,event):
		print "Exit"
		dlg = wx.MessageDialog(self,
		                       tcn('是否保存'+os.path.join(self.dirname,self.filename)),'MyEdit', 
							   wx.YES_NO |wx.CANCEL | wx.ICON_QUESTION)
		result =dlg.ShowModal()
		if result == wx.ID_YES:
			self.OnSave(event)
			dlg.Destroy()
			self.Close()
		elif result == wx.ID_NO:
			dlg.Destroy()
			self.Close()
		else:
			dlg.Destroy()
			
	def OnContact(self,event):
		import webbrowser 
		qq_url='http://wpa.qq.com/msgrd?v=3&uin=461829588&site=qq&menu=yes'
		webbrowser.open_new_tab(qq_url)  
		
	def OnAbout(self,event):
		description = '''
		None
		'''
		licence = '''  Notepad Easy is free software; you can redistribute
		it and/or modify it under the terms of the GNU General Public License as
		published by the Free Software Foundation'''
		info = wx.AboutDialogInfo()
		info.SetName('Notepad easy')
		info.SetIcon(wx.Icon('./images/we.png', wx.BITMAP_TYPE_PNG))
		info.SetVersion('1.0')
		info.SetDescription(description)
		info.SetCopyright('(C) 2013 - 2014 shalk')
		info.SetWebSite('http://www.weibo.com/xshalk')
		info.SetLicence(licence)
		info.AddDeveloper('shalk')
		info.AddDocWriter('shalk')
		info.AddArtist('shalk')
		info.AddTranslator('shalk')
		wx.AboutBox(info)
	#-------helper-----------
	

def tcn(data):
	return unicode(data,'gb2312','ignore')
	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MainWindow(None,-1,'Hello Vicki')
	frame.Show()
	app.MainLoop()
