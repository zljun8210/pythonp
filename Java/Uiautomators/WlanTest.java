/*2013.10.29
*
* JavaSE: 1.7
* Devices for ebent7/ebens1
* 
* v0.1: create wifi test;
* 
* function:
* 1. open wifiSettings
* 2. wifi on and connect (Stress testing)
* 3. wifi off
* 4. screencap save to sdcard with stress test 
* 
*/
package com.ebensz.wifitest;


import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiScrollable;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class WifiConn extends UiAutomatorTestCase 
{
static String SSID = "QAC_TS";
static String PASSWORD = "8888888888";
public void testDemo() throws UiObjectNotFoundException
{
startApp();
startUiTest();
} 

private void startApp() throws UiObjectNotFoundException
{
     // click Home 
        getUiDevice().pressHome();
  
        // select All Apps
        UiObject allAppsButton = new UiObject(new UiSelector().description("Apps"));
  
        // click all apps
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
        
       
}
private void startUiTest() throws UiObjectNotFoundException
{
//click WLAN switch wifiOn
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
sleep(10000);
// test wlan-connected
wlanOnOff(5);
// clear network connect
wifiSsid.click();
UiObject forgetBotton = new UiObject(new UiSelector().text("Forget"));
forgetBotton.click();
// close network
getUiDevice().click(150,150);
sleep(2000);
getUiDevice().pressHome();
}
private void wlanOnOff(int count) throws UiObjectNotFoundException
{
// wlan-network is on
SimpleDateFormat idf = new SimpleDateFormat("yyyy_MM_dd_HH_mm_ss");
String SCREEN_SHOT_PATH = "/sdcard/wifionoff_" + idf.format(new Date()) + "_";
int i = 1 ;
for (; i <= count; i++)
{
// close wlan-network
getUiDevice().click(150,150);
sleep(2000);
// open network
getUiDevice().click(150,150);
sleep(6000);
File screenPath = new File(SCREEN_SHOT_PATH + i + ".png");
getUiDevic
e().takeScreenshot(screenPath);
}
}
}