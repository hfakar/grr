#!/usr/bin/env python
"""The blob store abstraction."""


from future.utils import with_metaclass

from grr_response_core.lib import registry


class Blobstore(with_metaclass(registry.MetaclassRegistry, object)):
  """The blob store base class."""

  def StoreBlob(self, content, token=None):
    return self.StoreBlobs([content], token=token)[0]

  def ReadBlob(self, identifier, token=None):
    return self.ReadBlobs([identifier], token=token)[identifier]

  def BlobExists(self, identifier, token=None):
    return self.BlobsExist([identifier], token=token)[identifier]

  def StoreBlobs(self, contents, token=None):
    """Creates or overwrites blobs.

    Args:
      contents: A list containing data for each blob to be stored.
      token: Data store token.

    Returns:
      A list of identifiers, one for each stored blob.
    """

  def ReadBlobs(self, identifiers, token=None):
    """Reads blobs.

    Args:
      identifiers: A list of identifiers for the blobs to retrieve.
      token: Data store token.

    Returns:
      A dict mapping each identifier to the contents of this blob as a string
      or None if the blob doesn't exist.
    """

  def BlobsExist(self, identifiers, token=None):
    """Checks if blobs for the given identifiers already exist.

    Args:
      identifiers: A list of identifiers for the blobs to check.
      token: Data store token.

    Returns:
      A dict mapping each identifier to a boolean value indicating existence.
    """
