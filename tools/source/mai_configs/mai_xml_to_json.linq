<Query Kind="Program">
  <NuGetReference>Newtonsoft.Json</NuGetReference>
  <Namespace>Newtonsoft.Json</Namespace>
  <Namespace>Newtonsoft.Json.Bson</Namespace>
  <Namespace>Newtonsoft.Json.Converters</Namespace>
  <Namespace>Newtonsoft.Json.Linq</Namespace>
  <Namespace>Newtonsoft.Json.Schema</Namespace>
  <Namespace>Newtonsoft.Json.Serialization</Namespace>
  <Namespace>System.Xml.Serialization</Namespace>
</Query>

public class StringID
{ 
	public int id;
	public string str;
}

public class StringsCollection{
	public StringID[] list;
}

public class MusicGroupData
{
	public StringID name;
	public StringsCollection MusicIds;
	public string dataName;
}

public class JsonMusicGroupData{
	public string name;
	public StringID[] music_ids;
	
	public JsonMusicGroupData(MusicGroupData d){
		name = d.name.str;
		music_ids = d.MusicIds.list;
	}
	
}

public static bool Deserialize<T>(string filePath, out T dsr) where T : new()
{
	bool result = false;
	try
	{
		XmlDocument xmlDocument = new XmlDocument();
		xmlDocument.PreserveWhitespace = true;
		xmlDocument.Load(filePath);
		if (xmlDocument.DocumentElement == null)
		{
			throw new Exception("doc.DocumentElement == null");
		}
		XmlNodeReader xmlReader = new XmlNodeReader(xmlDocument.DocumentElement);
		XmlSerializer xmlSerializer = new XmlSerializer(typeof(T));
		dsr = (T)((object)xmlSerializer.Deserialize(xmlReader));
		result = true;
	}
	catch (Exception)
	{
		dsr = Activator.CreateInstance<T>();
		result = false;
	}
	return result;
}

void Main()
{
	var p = @"D:\Github\GoBot\plugins\nonebot-plugin-maimaidx\tools\source\mai_configs";
	var fs = Directory.GetFiles(p,"*.xml",SearchOption.AllDirectories);
	
	foreach(var f in fs){
		var x = Deserialize<MusicGroupData>(f,out var d);
		var jd = new JsonMusicGroupData(d);
		var parent = Path.GetDirectoryName(f);
		var fName = Path.GetFileNameWithoutExtension(f);
		var s = JsonConvert.SerializeObject(jd, Newtonsoft.Json.Formatting.Indented);
		File.WriteAllText(parent + "/" + fName + ".json",s);
	}
	
}

// You can define other methods, fields, classes and namespaces here
