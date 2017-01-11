/*	
 * 	Copyright (C)2013  Ebensz Auto Test
 * 
 * 		create by jack@ebensz.com
 * 
 * 	V0.2(20131108): optimize and Refactoring code:With an array called;
 * 	V0.1(20131105): create this program;
 * 
 * 	Function:
 * 		1. connect wlan network;
 * 		2. set launage;
 * 		3. run apps;
 * 		4. screencap to sdcard;
 * 
 */

package com.ebensz.regressiontest;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiScrollable;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class AppTest extends UiAutomatorTestCase 
{
	// set varilable
	static String SSID = "QAC_TS";
	
	static String PASSWORD = "8888888888";
	
	static String[] LEFT_SCREEN_NAME = {"Camera","device","People","Messaging","EReader","Eben Security Guards",
		"Gallery"};
	
	static String[] MID_SCREEN_NAME = {"Handwriting suite","Calendar","HwOffice","Browser","HwMail"};
	
	public void testDemo() throws UiObjectNotFoundException
	{
		// press home key
		int i;
		
		getUiDevice().pressHome();
		
		wifiConnect();
		
		deviceInfo();
		
		for (i=0; i<=LEFT_SCREEN_NAME.length; i++)
		{
			leftMove();
			
			startLaunchApk(LEFT_SCREEN_NAME[i]);
		}
		
		for (i=0; i<=MID_SCREEN_NAME.length; i++)
		{
			startLaunchApk(MID_SCREEN_NAME[i]);
		}

		startAllApp("EnoteWriter");
		
		startAllApp("ThemeController");
				
	}
	
	private void wifiConnect() throws UiObjectNotFoundException
	{
		getUiDevice().pressHome();
		
		// select all apps
		UiObject allAppsButton = new UiObject(new UiSelector().description("Apps"));
		
		allAppsButton.clickAndWaitForNewWindow();
		
        // select all apps tab
        UiObject appsTab = new UiObject(new UiSelector().text("Apps"));
  
        // click all apps tab
        appsTab.click();
  
        // set screen display mode
        UiScrollable appViews = new UiScrollable(new UiSelector().scrollable(true));
  
        // set horiz mode
        // appViews.setAsHorizontalList();
  
        if (allAppsButton.exists() && allAppsButton.isEnabled()) {
            // allAppsButton not display,don't exec it
            allAppsButton.click();
        }
        // find "settings" and click it
        UiObject settingsApp = appViews.getChildByText(
                new UiSelector().className(android.widget.TextView.class.getName()), "Settings");
        settingsApp.clickAndWaitForNewWindow();
  
        // verify Open screen is Settings
  
        UiObject settingsValidation = new UiObject(new UiSelector().packageName("com.android.settings"));
        // if not exists,then print error message
        assertTrue("Unable to detect Settings", settingsValidation.exists());
        
		 //	click WLAN switch wifiOn
        UiObject wifiText = new UiObject(new UiSelector().text("WLAN"));
        
        wifiText.click();
        
        getUiDevice().click(150,150);
        
        sleep(2000);
        
        UiObject wifiSsid = new UiObject(new UiSelector().text(SSID));
        
        wifiSsid.click();
        
        // set the SSID's  password
		UiObject passWord = new UiObject(new UiSelector().index(1).className("android.widget.EditText"));
		
		passWord.setText(PASSWORD);
		
		// connect the network
		UiObject connBotton = new UiObject(new UiSelector().text("Connect"));
		
		connBotton.click();
		
		sleep(2000);
		
		getUiDevice().pressHome();
	}

	private void deviceInfo() throws UiObjectNotFoundException
	{
		getUiDevice().pressHome();
		
		// select all apps
		UiObject allAppsButton = new UiObject(new UiSelector().description("Apps"));
		
		allAppsButton.clickAndWaitForNewWindow();
		
        // select all apps tab
        UiObject appsTab = new UiObject(new UiSelector().text("Apps"));
  
        // click all apps tab
        appsTab.click();
  
        // set screen display mode
        UiScrollable appViews = new UiScrollable(new UiSelector().scrollable(true));
  
        // set horiz mode
        // appViews.setAsHorizontalList();
  
        if (allAppsButton.exists() && allAppsButton.isEnabled()) {
            // allAppsButton not display,don't exec it
            allAppsButton.click();
        }
        // find "settings" and click it
        UiObject settingsApp = appViews.getChildByText(
                new UiSelector().className(android.widget.TextView.class.getName()), "Settings");
        settingsApp.clickAndWaitForNewWindow();
  
        // verify Open screen is Settings
  
        UiObject settingsValidation = new UiObject(new UiSelector().packageName("com.android.settings"));
        // if not exists,then print error message
        assertTrue("Unable to detect Settings", settingsValidation.exists());
        
        getUiDevice().swipe(100,900,100,200,2);
        
        UiObject devicesInfo = new UiObject(new UiSelector().text("About phone"));
        
        devicesInfo.click();
        
        sleep(500);
        
        Screencap("deviceInfo");
        
        sleep(1000);
        
        getUiDevice().pressHome();
	}
	
	private void startLaunchApk(String apks) throws UiObjectNotFoundException
	{
		// move to left home page
		//leftMove();
		
		UiObject apksButton = new UiObject(new UiSelector().text(apks));
		
		apksButton.clickAndWaitForNewWindow();
		
		Screencap(apks);
		
		getUiDevice().pressBack();
		
		getUiDevice().pressHome();
		
	}
	
	private void startAllApp(String apks) throws UiObjectNotFoundException
	{
		//	run all apps page apk
		//	press home key
		getUiDevice().pressHome();
		
		// select all apps
		UiObject allAppsButton = new UiObject(new UiSelector().description("Apps"));
		
		allAppsButton.clickAndWaitForNewWindow();
		
        // select all apps tab
        UiObject appsTab = new UiObject(new UiSelector().text("Apps"));
  
        // click all apps tab
        appsTab.click();
  
        // set screen display mode
        UiScrollable appViews = new UiScrollable(new UiSelector().scrollable(true));
  
        // set horiz mode
        // appViews.setAsHorizontalList();
  
        if (allAppsButton.exists() && allAppsButton.isEnabled()) {
            // allAppsButton not display,don't exec it
            allAppsButton.click();
        }
        // find "settings" and click it
        UiObject startApps = appViews.getChildByText(
                new UiSelector().className(android.widget.TextView.class.getName()), apks);
        startApps.clickAndWaitForNewWindow();
        
        sleep(2000);
        
        Screencap(apks);
        
        getUiDevice().pressBack();
        
        getUiDevice().pressHome();
	}
	
	private void leftMove() throws UiObjectNotFoundException
	{
		// press home key
		getUiDevice().pressHome();
		
		getUiDevice().pressHome();
		
		sleep(1000);
				
		getUiDevice().swipe(200,500,700,500,2);
		
		sleep(1000);
	}
	
 	private void Screencap(String apps) throws UiObjectNotFoundException
	{
		SimpleDateFormat idt = new SimpleDateFormat("yyyy_MM_dd_HH_mm_ss");
		
		String SCREENCAP_PATH = "/sdcard/EAT/" + apps + "_" + idt.format(new Date());
		
		File screen_path = new File(SCREENCAP_PATH + ".png");
		
		sleep(1000);
		
		getUiDevice().takeScreenshot(screen_path);
		
		assertTrue("Screenshot file not detected in store", screen_path.exists());
		
		sleep(1000);
	}
}
