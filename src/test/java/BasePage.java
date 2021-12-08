import com.thoughtworks.gauge.Step;
import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import org.apache.log4j.Logger;
import org.junit.Assert;
import org.openqa.selenium.By;

import java.util.List;
import java.util.Random;

import static io.appium.java_client.touch.offset.PointOption.point;

public class BasePage extends BaseTest {

    final static Logger logger = Logger.getLogger(BasePage.class.getName());


    @Step("<wait> saniye bekle")
    public void waitSecond(int wait) throws InterruptedException {
        Thread.sleep(1000 * wait);
        logger.info(wait + " SURE BEKLENDI");
    }

    @Step("<idClick> id'li elemante tikla")
    public void clickById(String idClick) {
        appiumDriver.findElement(By.id(idClick)).click();
        logger.info(idClick + " ID ELEMENTINE TIKLANDI");
    }

    @Step("<xpathClick> elemente tikla")
    public void clickByXpath(String xpathClick) {
        appiumDriver.findElement(By.xpath(xpathClick)).click();
        logger.info(xpathClick + " XPATH ELEMENTINE TIKLANDI");

    }


}














