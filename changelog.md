
# Changelog

## [1.3.5] - 14 December 2020

### Changed

- bug fixing of get_versions method


## [1.3.4] - 14 December 2020

### Changed

- mglib.storage.get_versions(self, doc_path) method added

## [1.3.3] - 14 December 2020

### Changed

- mglib.path module adjusted to accept version argument. Supports
    getting/setting path to versioned documents.

## [1.3.2] - 1 December 2020

### Changed

 - mglib.pdfinfo.get_pagecount use python magic + file extention to determine correct mime type (and thus page count)

## [1.3.1] - 1 December 2020

### Changed

- pdftk module was replaced with stapler


## [1.2.8] - 24 August 2020

### Added

- mglib.exceptions module introduced


## [1.2.7] - 17 August 2020

### Changed

- Do not raise exception when encoutering unsafe extention, log warning message instead.

## [1.2.6] - 11 August 2020

### Added

- mglib.conf.settings module. The points it to get rid of hardcoded binary paths. Binary paths are now provided as configurations.


## [1.2.3] - 25 July 2020

### Changed

  - bugfix - get_pagecount handles non utf-8 encoded documents

### Added

- unit tests for get_pagecount

## [1.2.1] - 16 July 2020

### Added
 
  - shortcuts.resize_img - resizes/converts images jpg, png documents
  - change get_pagecount to work with tiff files as well
  - bring in last modules from pmworker (mime and wrapper)

## [1.1.0] - 25 June 2020

### Added 
    - utils.try_load_config
    - utils.load_config
    - Endpoint module move in (from pmworker)

## [1.0.0] - 25 Apr 2020

### Hello, mglib!

