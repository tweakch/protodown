using System.Net;

WebClient webClient = new WebClient();
webClient.DownloadFile("http://mysite.com/myfile.txt", @"c:\myfile.txt");
