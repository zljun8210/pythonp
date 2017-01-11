    /*2013.10.30
 * 
 * JavaSE: 1.7
 * Copyright by jack@ebensz.com
 * 
 * V0.2: add screen shots to SDcard with date
 * V0.1: create the test;
 * 
 * Function:
 * 1. add account;
 * 
 */

package com.ebensz.mailtest;

import java.util.Date;
import java.text.SimpleDateFormat;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
//import com.android.uiautomator.core.UiScrollable;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;

public class AddAccount extends UiAutomatorTestCase 
{
		static SimpleDateFormat ift = new SimpleDateFormat("yyyy_MM_dd_HH_mm_ss");
		static String ACCOUNT = "277099728@qq.com";
		static String PASSWORD = "dgccjsj2008.";
		static String SERVER = "ex.qq.com";
		private static final String SCREEN_SHOT_NAME_PATH = "/sdcard/mailtest_addaccount_check_" + ift.format(new Date()) + ".png";
		private static final String SHELL_PM_COMM = "pm clear com.ebensz.email";
		public void testDemo() throws UiObjectNotFoundException, IOException, InterruptedException
		{
				getUiDevice().pressHome();
				//click HwMail 
				UiObject HwMail = new UiObject(new UiSelector().text("HwMail"));
				HwMail.clickAndWaitForNewWindow();
				//add account
				UiObject MailAddress = new UiObject(new UiSelector().description("Email address"));
				MailAddress.setText(ACCOUNT);
				//getUiDevice().pressKeyCode(61);
				UiObject Password =new UiObject(new UiSelector().description("Password"));
				Password.setText(PASSWORD);
				File storePath = new File(SCREEN_SHOT_NAME_PATH);
				getUiDevice().takeScreenshot(storePath);
				assertTrue("Screenshot image save done", storePath.exists());
				//click Next Bottom
				UiObject nextBottom = new UiObject(new UiSelector().text("Next"));
				nextBottom.clickAndWaitForNewWindow();
				//manual setup by Exchangeprotocol
				UiObject manBottom = new UiObject(new UiSelector().text("Manual setup"));
				manBottom.clickAndWaitForNewWindow();
				UiObject exchangeBottom = new UiObject(new UiSelector().text("Exchange"));
				exchangeBottom.clickAndWaitForNewWindow();
				UiObject serverEdit = new UiObject(new UiSelector().descriptionContains("Server"));
				serverEdit.click();
				getUiDevice().pressBack();
				UiObject manualNextBottom = new UiObject(new UiSelector().text("Next"));
				manualNextBottom.clickAndWaitForNewWindow();
				//This Done page
				UiObject accName = new UiObject(new UiSelector().description("Give this account a name (optional)"));
				accName.click();
				getUiDevice().pressBack();
				getUiDevice().swipe(200, 900, 200, 200, 2);
				UiObject doneBottom = new UiObject(new UiSelector().text("Done"));
				doneBottom.clickAndWaitForNewWindow();
				//mail page
				UiObject imageView1 = new UiObject(new UiSelector().clickable(true)); 
				imageView1.clickAndWaitForNewWindow();
				UiObject imageClick = new UiObject(new UiSelector().clickable(true).index(2));
				imageClick.clickAndWaitForNewWindow();
				//wait mail display
				UiObject inboxTextView = new UiObject(new UiSelector().text("Inbox"));
				inboxTextView.click();
				//screen shot
				File donePath = new File(SCREEN_SHOT_NAME_PATH);
				getUiDevice().takeScreenshot(donePath);
				assertTrue("Screenshot image save done", storePath.exists());
				getUiDevice().pressBack();
				// clear email data
				runShellCommand(SHELL_PM_COMM);
		}
    /**
     * Helper to execute a command on the shell
     *
     * @throws IOException
     * @throws InterruptedException
     */
    private void runShellCommand(String command) throws IOException, InterruptedException {
        Process p = null;
        BufferedReader resultReader = null;
        try {
            p = Runtime.getRuntime().exec(command);
            int status = p.waitFor();
            if (status != 0) {
                throw new RuntimeException(String.format("Run shell command: %s, status: %s",
                        command, status));
            }
        } finally {
            if (resultReader != null) {
                resultReader.close();
            }
            if (p != null) {
                p.destroy();
            }
        }
    }
}