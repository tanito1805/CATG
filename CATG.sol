// SPDX-License-Identifier: MIT
// Compatible with OpenZeppelin Contracts ^5.0.0
pragma solidity ^0.8.27;

import {ERC721} from "@openzeppelin/contracts@5.3.0/token/ERC721/ERC721.sol";
import {ERC721Enumerable} from "@openzeppelin/contracts@5.3.0/token/ERC721/extensions/ERC721Enumerable.sol";
import {ERC721URIStorage} from "@openzeppelin/contracts@5.3.0/token/ERC721/extensions/ERC721URIStorage.sol";
import {Ownable} from "@openzeppelin/contracts@5.3.0/access/Ownable.sol";

contract CATG is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {

    mapping(uint256 => uint256) public claims;
    uint256 public constant CLAIM_PERIOD = 30 days;

    constructor(address initialOwner)
        ERC721("CATG", "CATG")
        Ownable(initialOwner)
    {}

    function safeMint(address to, uint256 tokenId, string memory uri)
        public
        onlyOwner
    {
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    /// @notice Démarre une réclamation pour un token perdu
    function claim(uint256 tokenId) external onlyOwner {
    require(claims[tokenId] == 0, "Claim already in progress");
    claims[tokenId] = block.timestamp;
    }

    /// @notice Le contractOwner finalise la réclamation si aucun mouvement depuis 30 jours
    function finalizeClaim(uint256 tokenId) external onlyOwner {
    require(claims[tokenId] != 0, "No active claim");
    require(block.timestamp >= claims[tokenId] + CLAIM_PERIOD, "Claim period not over");

    address currentOwner = ownerOf(tokenId);
    _transfer(currentOwner, owner(), tokenId);
    claims[tokenId] = 0; // reset la réclamation
    }

    /// @notice Permet au propriétaire réel d’annuler la réclamation s’il récupère l’accès
    function cancelClaim(uint256 tokenId) external {
    require(claims[tokenId] != 0, "No active claim");
    require(msg.sender == ownerOf(tokenId), "Only the token owner can cancel the claim");

    claims[tokenId] = 0;
    }

    // The following functions are overrides required by Solidity.
    function _update(address to, uint256 tokenId, address auth)
        internal
        override(ERC721, ERC721Enumerable)
        returns (address)
    {
        return super._update(to, tokenId, auth);
    }

    function _increaseBalance(address account, uint128 value)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._increaseBalance(account, value);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}