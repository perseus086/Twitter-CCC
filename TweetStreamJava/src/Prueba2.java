import java.io.IOException;

import twitter4j.FilterQuery;
import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;


public class Prueba2 {

	
	
	public static void main(String[] args) throws TwitterException, IOException{
		
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true)
		.setOAuthConsumerKey("6Zyv4XxVypDqHDpFoHwSTrMzX")
		.setOAuthConsumerSecret("3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC")
		.setOAuthAccessToken("153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq")
		.setOAuthAccessTokenSecret("WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO");

		
		
		StatusListener listener = new StatusListener(){
			
			ConnectToDB db = new ConnectToDB();
			int i = 0;
			public void onStatus(Status status) {
	            i++;
	        	System.out.println(i+"]"+
	        			status.getUser().getName() + " : " + status.getText() + "["+status.getCreatedAt()+"]"+status.getId()+ status.getGeoLocation());
	        	db.save(status);
			
			}
	        public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) {}
	        public void onTrackLimitationNotice(int numberOfLimitedStatuses) {}
	        public void onException(Exception ex) {
	            ex.printStackTrace();
	        }
			
			@Override
			public void onScrubGeo(long arg0, long arg1) {
				// TODO Auto-generated method stub
				
			}
			@Override
			public void onStallWarning(StallWarning arg0) {
				// TODO Auto-generated method stub
				
			}
			
	    };
	    
	    TwitterStream twitterStream = new TwitterStreamFactory(cb.build()).getInstance();
	    twitterStream.addListener(listener);
	    // sample() method internally creates a thread which manipulates TwitterStream and calls these adequate listener methods continuously.
	   // double [][] location = {{ -38.442818d, 143.979651d }, {-37.672936d, 145.539709d }};
	    double [][]location = { { 144.3945d,-38.2607d},{145.7647d,-37.4598d } };
	    twitterStream.filter(new FilterQuery().locations(location));
	   
	}

}
