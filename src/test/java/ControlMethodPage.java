import com.thoughtworks.gauge.Step;
import org.apache.log4j.Logger;
import org.junit.Assert;
import org.openqa.selenium.By;

public class ControlMethodPage extends BaseTest {
    final static Logger logger = Logger.getLogger(BasePage.class.getName());


    @Step("<key> değerini içerdiğni kontrol et")
    public void textControl(String key) {
        boolean Display = appiumDriver.findElement(By.xpath(key)).isDisplayed();
        logger.info("GEREKLI KONTROLLER DOGRULANDI");
    }

    @Step("<key> id'li element <keyword> text değerini içerdiğni kontrol et")
    public void textContol(String key, String keyword) {
        Assert.assertTrue("Doğrulama Hatası", appiumDriver.findElement(By.xpath(key)).getText().contains(keyword));
        logger.info("GEREKLI KONTROLLER DOGRULANDI");

    }
}
