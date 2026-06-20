// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract DocumentVerification {

    struct Document {

        string fileName;

        string fileHash;

        uint256 timestamp;

        address uploader;

    }

    mapping(string => Document) public documents;

    function uploadDocument(
        string memory _fileName,
        string memory _fileHash
    ) public {

        documents[_fileHash] = Document(
            _fileName,
            _fileHash,
            block.timestamp,
            msg.sender
        );
    }

    function verifyDocument(
        string memory _fileHash
    ) public view returns (

        string memory,
        uint256,
        address

    ) {

        Document memory doc =
            documents[_fileHash];

        return (
            doc.fileName,
            doc.timestamp,
            doc.uploader
        );
    }
}