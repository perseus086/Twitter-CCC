import org.lightcouch.CouchDbClient;
import org.lightcouch.CouchDbProperties;
import org.lightcouch.Response;




public class ConnectToDB {

	private CouchDbClient dbClient;
	
	public ConnectToDB(){

		CouchDbProperties properties = new CouchDbProperties()
			.setDbName("melbourne")//not use capital letters
			.setCreateDbIfNotExist(true)
			.setProtocol("http")
			.setHost("localhost")
			.setPort(5984);
		dbClient = new CouchDbClient(properties);
	}
	
	public Response save(Object o){

		Response res = dbClient.save(o);
		return res;
	}
	
}
