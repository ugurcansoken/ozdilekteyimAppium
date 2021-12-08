import com.thoughtworks.gauge.Step;
import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import org.apache.log4j.Logger;

import java.util.List;
import java.util.Random;

import static io.appium.java_client.touch.offset.PointOption.point;

public class ProductPage extends BaseTest{
    final static Logger logger = Logger.getLogger(BasePage.class.getName());

    @Step("Scrolldown yapılır")
    public void scrollDownProduct() {
        int startX = 538;
        int startY = 1966;
        int endX = 539;
        int endY = 385;
        TouchAction action = new TouchAction(appiumDriver);
        action.press(point(startX, startY))
                .moveTo(point(endX,endY))
                .release()
                .perform();
        int NewstartX = 544;
        int NewstartY = 1961;
        int NewendX = 539;
        int NewendY = 265;
        TouchAction actionn = new TouchAction(appiumDriver);
        actionn.press(point(NewstartX, NewstartY))
                .moveTo(point(NewendX,NewendY))
                .release()
                .perform();
        logger.info("2 KERE SCROLL YAPILDI");

    }
    @Step("<randomKey> ürün seçilir")
    public void randomProductClick(String randomKey){
        List<MobileElement> elements = appiumDriver.findElementsById(randomKey);
        Random rnd = new Random();
        int rndInt = rnd.nextInt(elements.size());
        elements.get(rndInt).click();
        logger.info("RANDOM SECIM YAPILDI");
    }
}
