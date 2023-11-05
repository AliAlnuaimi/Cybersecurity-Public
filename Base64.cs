//Encode a File to Base64
private static void Base64EncodeFile(string inputFile, string outputFile)
{
    byte[] data = File.ReadAllBytes(inputFile);
    string text = Convert.ToBase64String(data);
    File.WriteAllText(outputFile, text);
}

//Decode a File from Base64
private static void Base64DecodeFile(string inputFile, string outputFile)
{
    string text = File.ReadAllText(inputFile);
    byte[] data = Convert.FromBase64String(text);
    File.WriteAllBytes(outputFile, data);
}

//Encode a String to Base64
private static string Base64Encode(string plainText) 
{
    var plainTextBytes = System.Text.Encoding.UTF8.GetBytes(plainText);
    return System.Convert.ToBase64String(plainTextBytes);
}


//Decode a String to Base64
private static string Base64Decode(string base64EncodedData) 
{
    var base64EncodedBytes = System.Convert.FromBase64String(base64EncodedData);
    return System.Text.Encoding.UTF8.GetString(base64EncodedBytes);
}

//Check if a string is base64
private bool IsBase64String(string base64)
{
    base64 = base64.Trim();
    return (base64.Length % 4 == 0) && Regex.IsMatch(base64,@"^[a-zA-Z0-9\+/]*={0,3}$", RegexOptions.None);
}
