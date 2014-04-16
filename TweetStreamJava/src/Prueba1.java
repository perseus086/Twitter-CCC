

import java.util.Iterator;
import java.util.List;

import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.conf.ConfigurationBuilder;


public class Prueba1{
	
	private ConfigurationBuilder cb;
	private TwitterFactory tf;
	private void configure(){
		
		cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true)
		.setOAuthConsumerKey("6Zyv4XxVypDqHDpFoHwSTrMzX")
		.setOAuthConsumerSecret("3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC")
		.setOAuthAccessToken("153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq")
		.setOAuthAccessTokenSecret("WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO");
	}
	
	public static void main(String[] args){
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true)
		.setOAuthConsumerKey("6Zyv4XxVypDqHDpFoHwSTrMzX")
		.setOAuthConsumerSecret("3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC")
		.setOAuthAccessToken("153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq")
		.setOAuthAccessTokenSecret("WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO");
		
		TwitterFactory tf = new TwitterFactory(cb.build());
		Twitter twitter = tf.getInstance();
		
		Query query = new Query("#LDU");
		query.setCount(10);
		QueryResult result = null;
		
		try {
			result = twitter.search(query);
			for (Status status : result.getTweets()) {
		        System.out.println("@" + status.getUser().getScreenName() + ":" + status.getText() + "["+status.getCreatedAt()+"]"+status.getId());
		    }
			
			
		} catch (TwitterException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		

		
	}
}
