# Data-Collection-and-Feature-Extraction
 machine learning system that can be used to classify a PE binary file as malicious or benign
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <div class="container">
        <h1>Data Collection and Feature Extraction Project</h1>
        <h2>Documentation for <code>data-plots.py</code></h2>
        <h3>Overview</h3>
        <p>The <code>data-plots.py</code> script is part of the Data Collection and Feature Extraction project. It is designed to create visualizations for a dataset that contains features labeled as benign or malware.</p>
        <h3>Dependencies</h3>
        <ul>
            <li>Python 3</li>
            <li><code>pandas</code> library for data manipulation and analysis.</li>
            <li><code>matplotlib</code> library for creating static, interactive, and animated visualizations in Python.</li>
        </ul>
        <h3>Usage</h3>
        <p>The script can be run from the command line without any arguments:</p>
        <pre><code>python data-plots.py</code></pre>
        <p>Upon execution, the script performs the following actions:</p>
        <ol>
            <li>Reads a CSV file named <code>dataset.csv</code>, which should be present in the same directory as the script.</li>
            <li>The script expects the CSV file to contain a column named 'label' where <code>0</code> indicates benign data and <code>1</code> indicates malware.</li>
            <li>It then generates two bubble plots: one for benign data and one for malware data, displaying them side by side for comparison.</li>
        </ol>
        <h3>Outputs</h3>
        <p>A figure with two subplots:</p>
        <ul>
            <li>The left subplot is a bubble plot of the benign features.</li>
            <li>The right subplot is a bubble plot of the malware features.</li>
        </ul>
        <p>Both plots are displayed to the user using <code>matplotlib</code>'s <code>plt.show()</code> function.</p>
        <h3>Notes</h3>
        <p>Ensure that the CSV file is formatted correctly and includes the necessary 'label' column.</p>
        <p>The script is currently set to display the plots immediately. To save the plots to a file, modifications to the script are needed to use <code>plt.savefig()</code> before <code>plt.show()</code>.</p>
    </div>
            <h2>Documentation for <code>encode.py</code></h2>
        <h3>Overview</h3>
        <p>The <code>encode.py</code> script encodes features from a CSV file into a binary format based on a provided list of features. The encoded data is then written to a new CSV file.</p>
        <h3>Dependencies</h3>
        <ul>
            <li>Python 3</li>
            <li>Standard <code>csv</code> library that comes with Python.</li>
        </ul>
        <h3>Usage</h3>
        <p>The script is designed to be imported and used within another Python script. Below is an example of how to use the functions within the script:</p>
        <pre><code>
import encode

# Read the feature list from a text file
features = encode.read_feature_list_txt('features.txt')

# Encode the features from the input CSV and write to the output CSV
encode.encode_features_csv('input.csv', features, 'output.csv')
        </code></pre>
        <h3>Outputs</h3>
        <p>The script will generate an output CSV file with the following columns:</p>
        <ul>
            <li><code>md5hash</code>: The MD5 hash of the data entry.</li>
            <li>Encoded features: Binary representation of the presence (1) or absence (0) of features.</li>
            <li><code>label</code>: The label associated with the data entry.</li>
        </ul>
        <h3>Notes</h3>
        <p>It is important to have the input CSV and feature list text file correctly formatted to match the expectations of the script.</p>
        <p>The output CSV file will contain binary encoded features which can be used for further analysis or machine learning purposes.</p>
    </div>
            <h2>Documentation for <code>feature_read.py</code></h2>
        <h3>Overview</h3>
        <p>The <code>feature_read.py</code> script is designed to read and process features from a CSV file, ensuring that each feature is unique and consolidated appropriately.</p>
        <h3>Dependencies</h3>
        <ul>
            <li>Python 3</li>
            <li>No external libraries are required.</li>
        </ul>
        <h3>Usage</h3>
        <p>The script defines a function that can be imported and used within another Python script. Here is how the function can be utilized:</p>
        <pre><code>
import feature_read

# Read features from a CSV file and process them
unique_features = feature_read.read_features_csv('features.csv')
        </code></pre>
        <h3>Outputs</h3>
        <p>The function will return a set of unique features processed from the CSV file.</p>
        <h3>Notes</h3>
        <p>Ensure the CSV file is structured properly, with features listed in the expected columns.</p>
        <p>The script provides console output indicating progress as it processes each line of the CSV file.</p>
    </div>
            <h2>Documentation for <code>scan.py</code></h2>
        <h3>Overview</h3>
        <p>The <code>scan.py</code> script is designed to scan directories for files, compute MD5 hashes, and extract certain features from the files for further analysis.</p>
        <h3>Dependencies</h3>
        <ul>
            <li>Python 3</li>
            <li><code>os</code> module for interacting with the operating system.</li>
            <li><code>hashlib</code> for generating MD5 hashes.</li>
            <li><code>re</code> module for regular expression matching (if used in the rest of the script not shown).</li>
        </ul>
        <h3>Usage</h3>
        <p>The script defines functions that can be used to scan files and should be called from within another Python script or the Python shell. Here's an example:</p>
        <pre><code>
import scan

# Define the folders to scan
folders_to_scan = ['/path/to/folder1', '/path/to/folder2']

# Start the scanning process
scan.scan_files(folders_to_scan)
        </code></pre>
        <h3>Outputs</h3>
        <p>The script generates a CSV file named <code>features.csv</code> with MD5 hashes and extracted features of the scanned files.</p>
        <h3>Notes</h3>
        <p>Make sure to have write permissions for the directory where the script will create the <code>features.csv</code> file.</p>
        <p>The script may take some time to process depending on the number of files in the provided directories.</p>
    </div>
</body>
</html>
