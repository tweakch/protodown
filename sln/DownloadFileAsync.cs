private void start()
{
  WebClient webClient = new WebClient();
  webClient.DownloadFileCompleted += new AsyncCompletedEventHandler(Completed);
  webClient.DownloadProgressChanged += new DownloadProgressChangedEventHandler(ProgressChanged);
  webClient.DownloadFileAsync(new Uri("http://mysite.com/myfile.txt"), @"c:\myfile.txt");
}

private void ProgressChanged(object sender, DownloadProgressChangedEventArgs e)
{
  //progressBar.Value = e.ProgressPercentage;
}

private void Completed(object sender, AsyncCompletedEventArgs e)
{
  //MessageBox.Show("Download completed!");
}
