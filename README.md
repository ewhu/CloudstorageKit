# CloudstorageKit: Unified Cloud Storage Abstraction for Python
Cloud-agnostic storage made easy

CloudstorageKit is a Python library that provides a unified interface for interacting with various cloud storage services. The library simplifies the process of integrating cloud storage into your application, allowing you to focus on developing your core functionality rather than worrying about the underlying storage infrastructure.

The primary goal of CloudstorageKit is to abstract away the differences between various cloud storage services, providing a consistent API that can be used across different providers. This enables developers to write cloud-agnostic code, making it easier to switch between different storage services or use multiple services in parallel.

CloudstorageKit supports a wide range of features, including file upload and download, directory management, and metadata manipulation. The library is designed to be highly performant, scalable, and fault-tolerant, making it suitable for use in large-scale production environments.

Some of the key benefits of using CloudstorageKit include:
* Simplified cloud storage integration
* Consistent API across different providers
* Improved code portability and reusability
* Enhanced scalability and performance
* Reduced development time and effort

## Key Features

* **Multi-provider support**: CloudstorageKit supports multiple cloud storage providers, including Amazon S3, Microsoft Azure Blob Storage, Google Cloud Storage, and more
* **Unified API**: The library provides a consistent API that can be used across different providers, making it easy to switch between services or use multiple services in parallel
* **File upload and download**: CloudstorageKit provides efficient file upload and download capabilities, with support for resumable uploads and ranged downloads
* **Directory management**: The library allows you to create, delete, and list directories, as well as manage file permissions and access control lists (ACLs)
* **Metadata manipulation**: CloudstorageKit provides support for metadata manipulation, including tagging, categorization, and custom metadata
* **Error handling and retries**: The library includes built-in error handling and retry mechanisms to ensure reliability and fault tolerance
* **Performance optimization**: CloudstorageKit is optimized for performance, with support for concurrent requests, connection pooling, and caching

## Technology Stack

* **Python 3.7+**: CloudstorageKit is built using Python 3.7 and later versions
* **Boto3**: The library uses Boto3, a popular Python SDK for Amazon Web Services (AWS), to interact with AWS services
* **Azure SDK for Python**: CloudstorageKit uses the Azure SDK for Python to interact with Microsoft Azure services
* **Google Cloud Client Library for Python**: The library uses the Google Cloud Client Library for Python to interact with Google Cloud services
* **Requests**: CloudstorageKit uses the Requests library to make HTTP requests to cloud storage services
* **Pytest**: The library uses Pytest for unit testing and integration testing

## Installation

To install CloudstorageKit, you can use pip:

Alternatively, you can install from source by cloning the repository and running:

## Configuration

CloudstorageKit requires configuration to connect to your cloud storage services. You can configure the library using environment variables or a configuration file. The following environment variables are supported:
* `CLOUDSTORAGEKIT_AWS_ACCESS_KEY_ID`
* `CLOUDSTORAGEKIT_AWS_SECRET_ACCESS_KEY`
* `CLOUDSTORAGEKIT_AZURE_STORAGE_ACCOUNT`
* `CLOUDSTORAGEKIT_AZURE_STORAGE_ACCESS_KEY`
* `CLOUDSTORAGEKIT_GOOGLE_CLOUD_STORAGE_BUCKET`
* `CLOUDSTORAGEKIT_GOOGLE_CLOUD_STORAGE_CREDENTIALS`

You can also configure CloudstorageKit using a configuration file in JSON or YAML format. The configuration file should contain the following settings:
* `aws_access_key_id`
* `aws_secret_access_key`
* `azure_storage_account`
* `azure_storage_access_key`
* `google_cloud_storage_bucket`
* `google_cloud_storage_credentials`

## Usage

CloudstorageKit provides a simple and intuitive API for interacting with cloud storage services. Here's an example of how to use the library to upload a file to Amazon S3:

You can find comprehensive API documentation in the [CloudstorageKit API documentation](https://cloudstoragekit.readthedocs.io/en/latest/).

## Contributing

CloudstorageKit is an open-source project that welcomes contributions from the community. If you're interested in contributing, please follow these guidelines:

* Fork the repository and create a new branch for your changes
* Make sure to write unit tests and integration tests for your changes
* Submit a pull request with a clear description of your changes
* Engage with the community and respond to feedback and comments

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ewhu/CloudstorageKit/blob/main/LICENSE) file for details.

## Acknowledgements

CloudstorageKit was inspired by several open-source projects, including Boto3, Azure SDK for Python, and Google Cloud Client Library for Python. We would like to acknowledge the hard work and contributions of the developers and maintainers of these projects.